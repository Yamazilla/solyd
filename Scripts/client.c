#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>


int main(){
	int sock =0;
        
       struct sockaddr_in serv_addr;

	if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
	printf("Socket creation error!");
	return -1; 
	}

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(9999);

	inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr); 

	connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr));

	char message[1024];
	char buffer[1024];

	while (1) {
		printf("Write the message: ");
		fgets(message, 1024, stdin);
		send(sock, message, strlen(message), 0);	

		if(strcmp(message, "exit\n") == 0 ) {
			break;
}

		memset(buffer, 0, sizeof(buffer));
		
		read(sock, buffer, 1024);
		printf("server: %s\n", buffer);

	}
} 
