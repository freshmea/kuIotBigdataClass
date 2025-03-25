// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>
// #include <unistd.h>
// #include <arpa/inet.h>
// #include <sys/socket.h>
// #include<wiringPi.h>
// #include<softTone.h> 

// #define BUZZER_PIN 12

// // Buzzer sound list
// int oxtav[22] =  {0,131,147,165,175,196,220,247,262,294,330,350,92,440,494,524,558,659,699,784,880,988};

// int flag = 0;
// void SW_ISR1(void);

// int main(int argc, char *argv[])
// {
//     int serv_sock, clnt_sock;
// 	int buff, i;
//     int sw;

//     // set GPIO
//     wiringPiSetupGpio();           //BCM
//     pinMode(BUZZER_PIN, OUTPUT);

//     //set ISR
//     wiringPiISR(sw,INT_EDGE_RISING,&SW_ISR1);


//     // set socket
// 	struct sockaddr_in serv_addr, clnt_addr;
// 	socklen_t clnt_addr_size;
// 	if(argc!=2){
// 		printf("Usage : %s <port>\n", argv[0]);
// 		exit(1);
// 	}
	
//     // socket()
// 	serv_sock=socket(PF_INET, SOCK_STREAM, 0);
// 	if(serv_sock == -1)
// 		error_handling("socket() error");
	
// 	memset(&serv_addr, 0, sizeof(serv_addr));
// 	serv_addr.sin_family=AF_INET;
// 	serv_addr.sin_addr.s_addr=htonl(INADDR_ANY);	//INADDR_ANY > 0x00000000 : anyone can connet IP_adress
// 	serv_addr.sin_port=htons(atoi(argv[1]));
	
//     // bind()
// 	if(bind(serv_sock, (struct sockaddr*) &serv_addr, sizeof(serv_addr))==-1 )
// 		error_handling("bind() error"); 
	
//     // listen()
// 	if(listen(serv_sock, 5)==-1)
// 		error_handling("listen() error");
	
//     //accept
//     clnt_addr_size=sizeof(clnt_addr);
//     clnt_sock=accept(serv_sock, (struct sockaddr*)&clnt_addr,&clnt_addr_size);

//     if(clnt_sock==-1)
//         error_handling("accept() error");
//     else
//         printf("Connected client %d \n",i+1);


//     // read sw
//     while (1)
//     {
//         sw = read(clnt_sock,buff,);
//         if(flag == 1){
//             for (int i = 0; i < 22; i++)
//             {
//                 softToneWrite(BUZZER_PIN,oxtav[i]);
//             }
//         }
//         else if(flag == 0) softToneWrite(BUZZER_PIN, 0);
            
        
//     }
//     // close()
//     close(clnt_sock);
// 	close(serv_sock);
// 	return 0;
// }

// void error_handling(char *message)
// {
// 	fputs(message, stderr);
// 	fputc('\n', stderr);
// 	exit(1);
// }


// void SW_ISR1(void){
//     if(flag == 0){
//         flag = 1;
//     }
//     else if(flag == 1){
//         flag = 0;
//     }
// }