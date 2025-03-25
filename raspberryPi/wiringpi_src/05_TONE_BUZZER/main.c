#include<stdio.h>
#include<wiringPi.h>
#include<softTone.h>     //Tone

// BCM
#define LED1 23
#define LED2 24
#define LED3 25
#define LED4 1

#define SW1 4
#define SW2 17
#define SW3 27
#define SW4 22

#define BUZZER_PIN 12

void SW_ISR1(void);
void SW_ISR2(void);
void SW_ISR3(void);
void SW_ISR4(void);


int oxtav[22] =  {0,131,147,165,175,196,220,247,262,294,330,350,92,440,494,524,558,659,699,784,880,988};

int main(void){

    wiringPiSetupGpio();           //BCM
    pinMode(BUZZER_PIN, OUTPUT);
    pinMode(SW1, INPUT);
    pinMode(SW2, INPUT);
    pinMode(SW3, INPUT);
    pinMode(SW3, INPUT);

    //set ISR
    wiringPiISR(SW1,INT_EDGE_RISING,&SW_ISR1);
    wiringPiISR(SW2,INT_EDGE_RISING,&SW_ISR2);
    wiringPiISR(SW3,INT_EDGE_RISING,&SW_ISR3);
    wiringPiISR(SW4,INT_EDGE_RISING,&SW_ISR4);

    //set Tone
    softToneCreate(BUZZER_PIN);
    while (1)
    {   
    }
    return 0;
}

void SW_ISR4(void){
    softToneWrite(BUZZER_PIN,0);
}

void SW_ISR1(void){
    softToneWrite(BUZZER_PIN,262);
}

void SW_ISR2(void){
    softToneWrite(BUZZER_PIN,294);
}

void SW_ISR3(void){
    softToneWrite(BUZZER_PIN,330);
}