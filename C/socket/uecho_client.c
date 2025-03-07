#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <unistd.h>

void error_handling(char *message);

int main(int argc, char *argv[]) {
	int sock;
	struct sockaddr_in serv_addr;
	char message[30];
	int str_len;
	socklen_t adr_sz;

	if (argc != 3) {
		printf("Usage : %s <IP> <port>\n", argv[0]);
		exit(1);
	}

	sock = socket(PF_INET, SOCK_DGRAM, 0);
	if (sock == -1)
		error_handling("socket() error");

	memset(&serv_addr, 0, sizeof(serv_addr));
	serv_addr.sin_family = AF_INET;
	serv_addr.sin_addr.s_addr = inet_addr(argv[1]);
	serv_addr.sin_port = htons(atoi(argv[2]));

	while (1) {
		fputs("Input message(Q to quit): ", stdout);
		fgets(message, sizeof(message), stdin);

		if (!strcmp(message, "Q\n") || !strcmp(message, "q\n")) {
			break;
		}
		sendto(sock, message, strlen(message), 0, (struct sockaddr *)&serv_addr,
			   sizeof(serv_addr));
		adr_sz = sizeof(serv_addr);
		str_len = recvfrom(sock, message, sizeof(message) - 1, 0,
						   (struct sockaddr *)&serv_addr, &adr_sz);
		message[str_len] = 0;
		printf("Message from server: %s \n", message);
	}
	close(sock);

	return 0;
}

void error_handling(char *message) {
	fputs(message, stderr);
	fputc('\n', stderr);
	exit(1);
}