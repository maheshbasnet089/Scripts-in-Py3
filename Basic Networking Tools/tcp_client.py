import socket

target_host = ''
target_port = 9998

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send(b"reeya")

# receive some data
response = client.recv(4096)

print(response.decode())
client.close()
