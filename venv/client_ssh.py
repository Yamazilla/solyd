import paramiko

host = input("Set the HOST: ")
user = input("Set USERNAME: ")
passwd = input("Set PASSWORD: ")


client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)

while True:    
    stdin, stdout,stderr = client.exec_command(input("Command: "))
    for line in stdout.readlines():
        print(line.strip())

    errors = stderr.readlines()
    if errors:
        print(errors)