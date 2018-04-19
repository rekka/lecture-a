/**
 * Illustration of rounding errors and dependence of a result of finite
 * precision arithmetics on the order of operations.
 */
#include <stdio.h>

int main()
{
    double a = 1.0e16;
    double b = -1.0e16;
    double c = 1.0;

    printf("(a + b) + c = %f\n", (a + b) + c);
    printf("a + (b + c) = %f\n", a + (b + c));
    return 0;
}
