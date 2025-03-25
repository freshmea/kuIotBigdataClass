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

int main(void){

    wiringPiSetupGpio();           // BCM 기준

    int LED[4] = {LED1,LED2,LED3,LED4};
    int SW[4] = {SW1,SW2,SW3,SW4};
    for (int i = 0; i < 4; i++){
        pinMode(LED[i],OUTPUT);
        pinMode(SW[i],INPUT);
    }
    
    while (1)
    {
        for (int i = 0; i < 4; i++)
        {
            if(digitalRead(SW[i])) digitalWrite(LED[i],HIGH);
            else digitalWrite(LED[i],LOW);
        }
                
    }
    

    return 0;
}