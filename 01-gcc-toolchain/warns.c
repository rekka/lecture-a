/**
 * gcc by default does not warn even when some kinds of serious bugs are present.
 *
 * Use -Wall -Wextra command line flags when compiling!
 */
#include <stdio.h>
int main() {
    double x;
    printf("%f\n", x);  // unitialized variable (Undefined Behavior!)
}

int n(int i) {
    i;      // forgotten return + no effect
}
