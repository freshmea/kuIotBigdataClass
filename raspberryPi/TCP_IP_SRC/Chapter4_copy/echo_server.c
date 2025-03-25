#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include<pthread.h>

#define BUF_SIZE 1024
void error_handling(char *message);

// pthread 선언
void* thread_main(void* arg);


int serv_sock, clnt_sock;

int main(int argc, char *argv[])
{
	// soket set value
	struct sockaddr_in serv_addr, clnt_addr;
	socklen_t clnt_addr_size;

	//pthread set value
	pthread_t t_id;

	if(argc!=2){
		printf("Usage : %s <port>\n", argv[0]);
		exit(1);
	}
	
	serv_sock=socket(PF_INET, SOCK_STREAM, 0);
	if(serv_sock == -1)
		error_handling("socket() error");
	
	memset(&serv_addr, 0, sizeof(serv_addr));
	serv_addr.sin_family=AF_INET;
	serv_addr.sin_addr.s_addr=htonl(INADDR_ANY);	//INADDR_ANY > 0x00000000 : anyone can connet IP_adress
	serv_addr.sin_port=htons(atoi(argv[1]));
	
	if(bind(serv_sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr))==-1 )
		error_handling("bind() error"); 
	
	if(listen(serv_sock, 5)==-1)
		error_handling("listen() error");
	clnt_addr_size=sizeof(clnt_addr);

	for(int i=0;i<5;++i){
		clnt_sock=accept(serv_sock, (struct sockaddr*)&clnt_addr,&clnt_addr_size);
		if(clnt_sock==-1)
			error_handling("accept() error");
		else
			printf("Connected client \n");

		if(pthread_create(&t_id,NULL,thread_main,(void*)&clnt_sock)!=0)
			error_handling("phtread() error");
	}
	
	close(serv_sock);
	return 0;
}

void error_handling(char *message)
{
	fputs(message, stderr);
	fputc('\n', stderr);
	exit(1);
}

// phtread 정의
void* thread_main(void* arg){
	int socket = *((int *)arg);
	char message[BUF_SIZE];
	int str_len;

	while((str_len=read(socket,message,BUF_SIZE))!= 0)
		write(socket, message, str_len);	

	close(socket);
}

