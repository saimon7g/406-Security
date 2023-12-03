import socket
import Elliptic
import random

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect to the server
# host = '127.0.0.1'
# port = 12345
# client_socket.connect((host, port))

# # Receive the welcome message from the server
# message = client_socket.recv(1024)
# print(f"Received message from server: {message.decode('utf-8')}")

# # Close the connection with the server
# client_socket.close()

print("Hello World!")
(a,b,primeP,E,x,y)=Elliptic.get_a_b_p_x_y()
print("Hello World!")
print("a: ",a)
print("b: ",b)
print("p: ",primeP)
print("E: ",E)
print("x: ",x)
print("y: ",y)

privateKeyClient=random.randint(1,E-1)
print("Private Key Client: ",privateKeyClient)

privateKeyClient=5
x=5
y=1
primeP=17
a=2
b=2

nG=Elliptic.calculate_kG(privateKeyClient, x, y, a, primeP)
print("nG: ",nG)








# kG=Elliptic.calculate_kG(privateKeyClient, x, y, a, primeP)



