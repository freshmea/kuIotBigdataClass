#include<stdio.h>
#include<wiringPi.h>
#include<softPwm.h>     //PWM

// BCM
#define LED1 23
#define LED2 24
#define LED3 25
#define LED4 1

#define SW1 4
#define SW2 17
#define SW3 27
#define SW4 22

int main(void){
    wiringPiSetupGpio();           //BCM
    pinMode(LED1,OUTPUT);
    pinMode(LED2,OUTPUT);
    //set PWM
    softPwmCreate(LED1,255,255);
    softPwmCreate(LED2,0,255);

    while (1)
    {
        for (int i = 0; i < 255; i++)
        {
            
            softPwmWrite(LED2,i);
            delay(100);
        }
        
    }
    return 0;
}
