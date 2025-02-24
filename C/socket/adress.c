#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <sys/socket.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
	struct sockaddr_in addr;
	int sockfd;
	int len;
	int result;
	char ch = 'A';

	sockfd = socket(AF_INET, SOCK_STREAM, 0);

	// print byte size of AF_INET
	printf("AF_INET: %d\n", AF_INET);
	// print byte size of sa_family_t
	printf("__SOCKADDR_COMMON: %ld\n", sizeof(sa_family_t));

	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = inet_addr("127.0.0.1");
	addr.sin_port = htons(9734);
	len = sizeof(addr);
	result = bind(sockfd, (struct sockaddr *)&addr, len);
	if (result < 0) {
		perror("Bind failed");
		return -1;
	} else {
		printf("Bind success\n");
		listen(sockfd, 5);
		printf("Listening on port 9734\n");

		int client_sock = accept(sockfd, NULL, NULL);
		if (client_sock < 0) {
			perror("Accept failed");
			return -1;
		}
		printf("Client connected\n");

		char buffer[256];
		bzero(buffer, 256);
		read(client_sock, buffer, 255);
		printf("Received message: %s\n", buffer);

		close(client_sock);
	}

	close(sockfd);
	return 0;
}