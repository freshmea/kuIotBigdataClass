#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<unistd.h>
#include<arpa/inet.h>
#include<sys/socket.h>
void error_handling(char *message);

#define TRUE 1
#define FALSE 0

int main(int argc char* argv[]){

    int serv_sock, clnt_sock;
    char message[30];
    int option, str_len;
    struct sockaddr_in serv_addr, clnt_addr;
    socklen_t optlen, clnt_addr_sz;
    if(argc!=2){
        printf("Using : %s <port>\n", argv[0]);
        exit(1);
    }

    serv_sock=socket(PF_INET,SOCK_STREAM, 0);
    if(serv_sock==-1)
        error_handling("socket() error");

    optlen=sizeof(option);
    option=TRUE;
    setsockopt(serv_sock,SOL_SOCKET,SO_REUSEADDR,(void*)&option, optlen);

    memset(&serv_addr, 0 ,sizeof(serv_addr));
    serv_addr.sin_family=AF_INET;
    serv_addr.sin_addr.s_addr=htonl(INADDR_ANY);

}