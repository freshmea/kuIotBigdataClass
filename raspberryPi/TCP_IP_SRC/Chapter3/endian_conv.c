#include<stdio.h>
#include<stdlib.h>
#include<arpa/inet.h>


int main(int argc, char *argv[]){

    unsigned short host_port=0x1234;
    unsigned short net_port;
    unsigned long host_addr=0x12345678;
    unsigned long net_addr;

    net_port=htons(host_port);
    net_addr=htonl(host_addr);

    // printf("Host ordered port: %#x \n", host_port);
    // printf("Network order port: %#x \n", net_port);
    // printf("Host ordered address: %#x \n", host_addr);
    // printf("Network ordered address: %#x \n", net_addr);

    net_port=htons(atoi(argv[1]));
    net_addr=htonl(atoi(argv[2]));
    printf("Network order port: %#x \n", net_port);
    printf("Network ordered address: %#x \n", net_addr);
    return 0;
}