import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    while True:
        message = input("Message: ") + "\n"    
        client.sendto(message.encode(), ("127.0.0.1", 9000))
        data, sender = client.recvfrom(1024)
        print(sender[0] + ": " + data.decode())
        if data.decode() == "Terminate\n" or message == "Terminate\n":
            break

    client.close()
except Exception as error:
    print("An error has occurred.")
    print(error)
    client.close()