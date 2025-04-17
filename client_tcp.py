import socket



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(1)

try:
    client.connect(("127.0.0.1", 9003))
    client.send(b"Tovarischej\n")
    received_packages = client.recv(1024).decode()
    print(received_packages)
except:
    print("An error has occurred.")