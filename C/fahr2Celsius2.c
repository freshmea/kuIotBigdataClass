#include <stdio.h>

int main(void) {
	int fahr;
	double celsius;

	fahr = 100;
	celsius = 5.0 / 9.0 * (fahr - 32);
	// celsius = 5.0 / 9.0 * (fahr - 32);

	printf("fahr: %d ---> selsius: %.2f\n", fahr, celsius);
	return 0;
}
