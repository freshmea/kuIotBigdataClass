#include <arpa/inet.h>
#include <linux/sockios.h>
#include <netinet/in.h>
#include <stdio.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
	printf("INADDR_ANY: %d\n", INADDR_ANY);
	printf("INADDR_LOOPBACK: %d\n", INADDR_LOOPBACK);
	printf("AF_INET: 2\n");
	printf("__SOCKADDR_COMMON: 2\n");
	printf("AF_INET6: 10\n");
	printf("AF_UNIX: 1\n");

	int sock;
	int snd_buf, rcv_buf, state;
	socklen_t len;

	sock = socket(AF_INET, SOCK_STREAM, 0);
	len = sizeof(snd_buf);
	state = getsockopt(sock, SOL_SOCKET, SO_SNDBUF, &snd_buf, &len);
	if (state) {
		perror("getsockopt() error");
		return -1;
	}
	printf("Listening socket Send buffer size: %d\n", snd_buf);

	struct sockaddr_in addr, client_addr;
	addr.sin_family = AF_INET;
	addr.sin_addr.s_addr = inet_addr("0.0.0.0");
	addr.sin_port = htons(8080);

	if (bind(sock, (struct sockaddr *)&addr, sizeof(addr)) < 0) {
		perror("bind() error");
		return -1;
	}
	printf("Bind success\n");

	if (listen(sock, 5) < 0) {
		perror("listen() error");
		return -1;
	}

	int clientfd = accept(sock, (struct sockaddr *)&client_addr, &len);
	if (clientfd < 0) {
		perror("accept() error");
		return -1;
	}

	printf("Listening for connections...\n");
	char client_ip[INET_ADDRSTRLEN];
	inet_ntop(AF_INET, &client_addr.sin_addr, client_ip, sizeof(client_ip));
	printf("Client IP:%s\n", client_ip);
	printf("Client port:%d\n", ntohs(client_addr.sin_port));

	// clientfd 의 로컬 및 원격 포트 확인
	struct sockaddr_in local_addr, remote_addr;
	socklen_t addr_len = sizeof(local_addr);
	getsockname(clientfd, (struct sockaddr *)&local_addr, &addr_len);
	getpeername(clientfd, (struct sockaddr *)&remote_addr, &addr_len);
	printf("Server local IP: %s\n", inet_ntoa(local_addr.sin_addr));   //
	printf("Client remote IP: %s\n", inet_ntoa(remote_addr.sin_addr)); //
	printf("Server local port: %d\n", ntohs(local_addr.sin_port));	   // 8080
	printf("Client remote port: %d\n", ntohs(remote_addr.sin_port));   // 49152

	state = getsockopt(clientfd, SOL_SOCKET, SO_SNDBUF, &snd_buf, &len);
	if (state) {
		perror("getsockopt() error");
		return -1;
	}
	printf("Client socket Send buffer size: %d\n", snd_buf);

	// 데이터 송신 테스트
	char *message = "Hello, Client!";
	int bytes_sent = send(clientfd, message, strlen(message), 0);
	if (bytes_sent < 0) {
		perror("send() error");
		return -1;
	}
	printf("Sent %d bytes: %s\n", bytes_sent, message);

	// 송신 큐 크기 확인 (선택 사항)
	int outq;
	if (ioctl(clientfd, SIOCOUTQ, &outq) < 0) {
		perror("ioctl() error");
	} else {
		printf("Current send queue size: %d bytes\n", outq);
	}
	if (ioctl(sock, SIOCOUTQ, &outq) < 0) {
		perror("ioctl() error");
	} else {
		printf("Listening socket send queue size: %d bytes\n", outq);
	}

	// 클라이언트로부터 데이터 수신 (선택 사항)
	char buffer[1024];
	int bytes_received = recv(clientfd, buffer, sizeof(buffer) - 1, 0);
	if (bytes_received < 0) {
		perror("recv() error");
	} else {
		buffer[bytes_received] = '\0';
		printf("Received from client: %s\n", buffer);
	}

	close(clientfd);
	close(sock);
	return 0;
}