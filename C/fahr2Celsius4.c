#include <stdio.h>

int main(void)
{
	int fahr;
	//double celsius;
	
	fahr = 100;
	//celsius = 5.0 / 9.0 * (fahr*1.0 - 32);
	
	int celsius1000;
	celsius1000 = 1000 * 5 * (fahr - 32) / 9;
	//printf("celsius1000 : %d\n", celsius1000);
	
	int left = celsius1000 / 1000;
	int right = (celsius1000 - celsius1000 / 1000 * 1000 + 5) / 10;
	
	//printf("fahr: %d ---> celsius: %.2f\n", fahr, celsius);
	printf("fahr: %d ---> celsius: %d.%d\n", fahr, left, right);
	return 0;
}
