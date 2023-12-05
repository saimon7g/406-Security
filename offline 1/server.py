import socket
import threading
import pickle
import Elliptic

def handle_client(client_socket, addr):
    # Send a welcome
    message = "Welcome to the server!"
    serialized_message=pickle.dumps(message)
    client_socket.send(serialized_message)
    # Receive Hello
    res=client_socket.recv(1024)
    deserialized_response=pickle.loads(res)
    print(deserialized_response)
    # Send Hello
    message = "Hello client!"
    serialized_message=pickle.dumps(message)
    client_socket.send(serialized_message)
    

    while True:
        try:
            # Receive the shared parameters from client
            res=client_socket.recv(1024)
            deserialized_response=pickle.loads(res)
            a=deserialized_response['a']
            b=deserialized_response['b']
            p=deserialized_response['p']
            x=deserialized_response['x']
            y=deserialized_response['y']
            print("parameters: ",deserialized_response)
            # change key here 
            private_key=5
            
            public_key=Elliptic.calculate_kG(a,b,p,x,y,private_key)
            message = "Public key: "
            data={'message':message,'public_key':public_key}
            serialized_data=pickle.dumps(data)
            client_socket.sendall(serialized_data)
            # receive the public key from client
            res=client_socket.recv(1024)
            deserialized_response=pickle.loads(res)
            received_public_key=deserialized_response['public_key']
            print("received public key from client: ",received_public_key)
            encryption_key=Elliptic.calculate_kG(a,b,p,received_public_key[0],received_public_key[1],private_key)[0]
            print("encryption key at server: ",encryption_key)
            
            
            
        except ConnectionResetError:
            # Handle client disconnection
            print(f"Connection with {addr} closed")
            break

    # Close the connection with the client
    client_socket.close()
    print(f"Connection with {addr} closed and ended")




# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server port
host = '127.0.0.1'
port = 12345
server_socket.bind((host, port))
server_socket.listen(5)
print(f"Server listening on {host}:{port}")
while True:
    client_socket, addr = server_socket.accept()
    print(f"Got connection from {addr}")
    # Handle the client in a separate thread
    client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))
    client_thread.start()