#include<stdio.h>
#include<string.h>
#include<error.h>
#include<unistd.h>
#include<stdlib.h>
#include<stdint.h>
#include<time.h>

#include<wiringPi.h>
#include<wiringPiI2C.h>

int main(void){
    int temphumi = 0;
    uint8_t data[3] = {0};
    uint32_t val = 0;
    float temp;
    float humi;
    if((temphumi = wiringPiI2CSetup(0x40)) < 0){
        printf("SHT20 : Unable to initial I2C\n");
        return -1;
    }
    wiringPiI2CWrite(temphumi,0xfe);
    delay(50);   
    while (1)
    {
        //temp
        wiringPiI2CWrite(temphumi,0xf3);
        delay(260);

        for (int i = 0; i < 3; i++)
        {
            data[i] = wiringPiI2CRead(temphumi);
        }
        
        val= data[0] << 8 | data[1];
        temp = -46.85 + 175.72 * (int)val / 65536;
        printf("temp : %.1f\n",temp);

        // humi
        wiringPiI2CWrite(temphumi,0xf5);
        delay(60);

        for (int i = 0; i < 3; i++)
        {
            data[i] = wiringPiI2CRead(temphumi);
        }
        
        val= data[0] << 8 | data[1];
        humi = -6.0 + 125 * (int)val / 65536;
        printf("humi : %.1f\n",humi);

        delay(1000);
    }
    
    return 0;
}