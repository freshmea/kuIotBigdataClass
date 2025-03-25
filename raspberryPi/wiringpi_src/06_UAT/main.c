#include<stdio.h>
#include<string.h>
#include<error.h>
#include<wiringPi.h>
#include<wiringSerial.h>

int main(void){
    int serial_port;
    char dat;

    if((serial_port = serialOpen("/dev/ttyS0",115200)) < 0){    // dev name , speed
        printf("Unable to open serail device");
        return 1;
    }

    wiringPiSetup();

    serialPrintf(serial_port,"90",100);

    while (1)
    {
        if(serialDataAvail(serial_port)){
            dat = serialGetchar(serial_port);
            printf("%c",dat);
            fflush(stdout);
            serialPutchar(serial_port,dat);
        }
    }
    
    return 0;
}