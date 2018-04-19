#include <stdio.h>

int main()
{
    double a = 1.0e16;
    double b = -1.0e16;
    double c = 1.0;
    double d = 0.1;

    printf("(a + b) + c = %f\n", (a + b) + c);
    printf("a + (b + c) = %f\n", a + (b + c));
    printf("%f\n", (d * 10 - 1.)*1e15);
    return 0;
}
