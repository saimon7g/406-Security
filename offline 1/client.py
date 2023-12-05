import socket
import Elliptic
import random
import pickle


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
       
    while True:
        shared_parameters=Elliptic.get_parameters()
        a=shared_parameters[0]
        b=shared_parameters[1]
        p=shared_parameters[2]
        x=shared_parameters[3]
        y=shared_parameters[4]
        print("parameters: ",shared_parameters)
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
        
        
        
        

        
        
        hold=input("Press enter to continue")
        
        
        

    # Close the connection with the server
    client_socket.close()
    
client_programme()

