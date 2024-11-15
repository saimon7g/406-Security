import socket
import random
import pickle
import importlib

f1='1905056_ECC'
f2='1905056_AES'
Elliptic = importlib.import_module(f1)
AES = importlib.import_module(f2)   



def establish_key(client_socket):
    input_bits=input("input number of bits: ")
    shared_parameters=Elliptic.get_parameters(input_bits)
    a=shared_parameters[0]
    b=shared_parameters[1]
    p=shared_parameters[2]
    x=shared_parameters[3]
    y=shared_parameters[4]
    # print("parameters: ",shared_parameters)
    parameters={'a':a,'b':b,'p':p,'x':x,'y':y}
    serialized_parameters=pickle.dumps(parameters)
    client_socket.sendall(serialized_parameters)
    # receive the public key from server
    res=client_socket.recv(1024)
    deserialized_response=pickle.loads(res)
    received_public_key=deserialized_response['public_key']
    print("received public key from server: ",received_public_key)
    # change key here
    e=Elliptic.generate_E(p)
    private_key=random.randint(1,e)
    
    public_key=Elliptic.calculate_kG(a,b,p,x,y,private_key)
    # send the public key to server
    message = "Public key: "
    data={'message':message,'public_key':public_key}
    serialized_data=pickle.dumps(data)
    client_socket.sendall(serialized_data)
    # calculate the encryption key
    encryption_key=Elliptic.calculate_kG(a,b,p,received_public_key[0],received_public_key[1],private_key)[0]
    print("encryption key at client: ",encryption_key) 

    return encryption_key


def client_programme():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    host = '127.0.0.1'
    port = 12345
    try:
        client_socket.connect((host, port))
    except:
        print("Server is not running")
        exit()
    
    # Receive welcome from the server
    res=client_socket.recv(1024)
    deserialized_response=pickle.loads(res)
    print(deserialized_response)
    # send hello message to server
    first={"name":"client","message":"Hello server!"} 
    serialized_first=pickle.dumps(first)  
    client_socket.sendall(serialized_first)
    # receive hello message from server
    res=client_socket.recv(1024)
    deserialized_response=pickle.loads(res)
    print(deserialized_response)
    encryption_key=establish_key(client_socket)
       
    while True:
        try:       
            
            relayCipher=AES.task3_encryption(encryption_key)
            relayCipher=str(relayCipher)
            data={'relayCipher':relayCipher}
            serialized_data=pickle.dumps(data)
            client_socket.sendall(serialized_data)
            
            res=client_socket.recv(1024)
            cipher=pickle.loads(res)
            print("cipher received from server: ",cipher['relayCipher'])
            ciphermsg=cipher['relayCipher']
            plaintext=AES.task3_decryption(encryption_key,ciphermsg)
            print("plaintext: ",plaintext)
            
            
            
        except ConnectionResetError:
            # Handle server disconnection
            print("Connection with server closed")
            break
    
        hold=input("Press enter to continue")
        
        
        

    # Close the connection with the server
    client_socket.close()
    
client_programme()

