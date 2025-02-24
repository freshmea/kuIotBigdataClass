#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <sys/socket.h>

int main(int argc, char *argv[]) {
	struct sockaddr_in serv_addr;

	if (argc != 3) {
		fprintf(stderr, "Usage: %s <server_ip> <port>\n", argv[0]);
		exit(1);
	}

	int sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd < 0) {
		perror("ERROR opening socket");
		exit(1);
	}

	bzero((char *)&serv_addr, sizeof(serv_addr));
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(atoi(argv[2]));
	serv_addr.sin_addr.s_addr = inet_addr(argv[1]);

	if (connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
		perror("ERROR connecting");
		exit(1);
	}

	printf("Connected to server %s on port %s\n", argv[1], argv[2]);
	char *message = "Hello, World! this message from client\n";
	int size = strlen(message);
	send(sockfd, message, size, 0);
	close(sockfd);
	return 0;
}