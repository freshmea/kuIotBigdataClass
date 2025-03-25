#include<stdio.h>
#include<wiringPi.h>

// BCM
#define LED1 23
#define LED2 24
#define LED3 25
#define LED4 1

#define SW1 4
#define SW2 17
#define SW3 27
#define SW4 22

void SW_ISR(void);
 
int flag_led=0;    
int main(void){

    wiringPiSetupGpio();           
    pinMode(LED1,OUTPUT);
    pinMode(SW1,INPUT);
    
    // set extend interrupt
    wiringPiISR(SW1,INT_EDGE_RISING,&SW_ISR);


    while (1)
    {
    }
    

    return 0;
}

void SW_ISR(void){
    
    if (flag_led == 0){
        printf("SWITCH ON\n");
        digitalWrite(LED1,HIGH);
        flag_led = 1;
    }else{
        printf("SWITCH OFF\n");
        digitalWrite(LED1,LOW);
        flag_led = 0;
    }
}