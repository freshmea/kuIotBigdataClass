#include<stdio.h>
#include<wiringPi.h>

// BCM
// #define LED1 23
// #define LED2 24
// #define LED3 25
// #define LED4 1

// Phys
// #define LED1 16
// #define LED2 18
// #define LED3 22
// #define LED4 28

// wPi
#define LED1 4
#define LED2 5
#define LED3 6
#define LED4 31

int main(void){

    //wiringPiSetupGpio();           // BCM 기준
    // wiringPiSetupPhys();          // Phys 기준
    wiringPiSetup();                 // wPi 기준
    int LED[4] = {LED1,LED2,LED3,LED4};
    for (int i = 0; i < 4; i++){
        pinMode(LED[i],OUTPUT);}
    
    while (1)
    {
        for (int i = 0; i < 4; i++){
            digitalWrite(LED[i],HIGH);}
    
        delay(1000);
        for (int i = 0; i < 4; i++){
            digitalWrite(LED[i],LOW);}
        delay(1000);
    }
    

    return 0;
}