#include <stdio.h>

int main()
{
    double sum = 0.;
    for (int i = 0; i < 1000000000; i ++) {
        sum += i;
    }

    printf("%f\n", sum);

    return 0;
}
