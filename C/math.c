#include <math.h>
#include <stdio.h>

int main(void){
    double x = 2.0;
    double y = 3.0;
    double z = pow(x, y);
    double a = sqrt(x);
    double b = exp(x);
    double c = log(x);
    double d = log10(x);
    double e = fabs(-x);
    double f = ceil(x);
    printf("The result of %f raised to the power of %f is %f\n", x, y, z);
    printf("The square root of %f is %f\n", x, a);
    printf("The exponential of %f is %f\n", x, b);
    printf("The natural logarithm of %f is %f\n", x, c);
    printf("The base 10 logarithm of %f is %f\n", x, d);
    printf("The absolute value of %f is %f\n", -x, e);
    printf("The smallest integer value greater than or equal to %f is %f\n", x, f);
    return 0;
}