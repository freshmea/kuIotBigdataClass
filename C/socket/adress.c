#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <sys/socket.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
	struct sockaddr_in addr;
	struct sockaddr_in client_addr;
	int sockfd;
	int len;
	int result;
	char ch = 'A';

	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd < 0) {
		perror("Socket creation failed");
		return -1;
	} else {
		printf("Socket created\n %d", sockfd);
	}

	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = inet_addr("0.0.0.0");
	addr.sin_port = htons(9734);
	len = sizeof(addr);
	// reuse port
	int opt = 1;
	setsockopt(sockfd, SOL_SOCKET, SO_REUSEADDR, &opt, sizeof(opt));
	result = bind(sockfd, (struct sockaddr *)&addr, len);
	if (result < 0) {
		perror("Bind failed");
		return -1;
	} else {
		printf("Bind success\n");
		listen(sockfd, 5);
		printf("Listening on port 9734\n");

		len = sizeof(client_addr);

		int client_sock = accept(sockfd, (struct sockaddr *)&client_addr, &len);
		if (client_sock < 0) {
			perror("Accept failed");
			return -1;
		}
		printf("Client connected %d\n", client_sock);
		// print client socket ip, port
		printf("Client IP: %s\n", inet_ntoa(client_addr.sin_addr));
		printf("Client port: %d\n", ntohs(client_addr.sin_port));

		char buffer[256];
		bzero(buffer, 256);
		read(client_sock, buffer, 255);
		printf("Received message: %s\n", buffer);

		close(client_sock);
	}

	close(sockfd);
	return 0;
}