#include <stdio.h>
#define PI 3.141592

int main(void)
{
	int radius;

	printf("insert number\n");
	scanf("%d", &radius);
	
	double extent = radius * radius * PI;
	
	printf("extent is %f\n", extent);
	
	return 0;
}
