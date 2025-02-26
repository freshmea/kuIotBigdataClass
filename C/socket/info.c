#include <netinet/in.h>
#include <stdio.h>
#include <sys/socket.h>

int main(int argc, char *argv[]) {
	printf("INADDR_ANY: %d\n", INADDR_ANY);
	printf("INADDR_LOOPBACK: %d\n", INADDR_LOOPBACK);
	printf("AF_INET: 2\n");
	printf("__SOCKADDR_COMMON: 2\n");

	printf("AF_INET6: 10\n");
	printf("AF_UNIX: 1\n");

	return 0;
}