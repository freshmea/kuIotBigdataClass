#include <arpa/inet.h>
#include <netinet/in.h>
#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <sys/socket.h>
#include <unistd.h> // close() 함수를 위해 추가

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

	// connect 전 송신 버퍼 크기 확인
	int snd_buf;
	socklen_t len = sizeof(snd_buf);
	if (getsockopt(sockfd, SOL_SOCKET, SO_SNDBUF, &snd_buf, &len) < 0) {
		perror("getsockopt() before connect error");
		exit(1);
	}
	printf("Send buffer size before connect: %d bytes\n", snd_buf);

	bzero((char *)&serv_addr, sizeof(serv_addr));
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(atoi(argv[2]));
	serv_addr.sin_addr.s_addr = inet_addr(argv[1]);

	if (connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
		perror("ERROR connecting");
		exit(1);
	}

	// connect 후 송신 버퍼 크기 확인
	if (getsockopt(sockfd, SOL_SOCKET, SO_SNDBUF, &snd_buf, &len) < 0) {
		perror("getsockopt() after connect error");
		exit(1);
	}
	printf("Send buffer size after connect: %d bytes\n", snd_buf);

	// 클라이언트 소켓 IP와 포트 출력
	struct sockaddr_in client_addr;
	socklen_t client_len = sizeof(client_addr);
	if (getsockname(sockfd, (struct sockaddr *)&client_addr, &client_len) < 0) {
		perror("getsockname() error");
		exit(1);
	}
	printf("Client IP: %s\n", inet_ntoa(client_addr.sin_addr));
	printf("Client port: %d\n", ntohs(client_addr.sin_port));

	printf("Connected to server %s on port %s\n", argv[1], argv[2]);

	// 데이터 송신
	char *message = "Hello, World! this message from client\n";
	int size = strlen(message);
	if (send(sockfd, message, size, 0) < 0) {
		perror("send() error");
		exit(1);
	}
	printf("Sent message: %s", message);

	close(sockfd);
	return 0;
}