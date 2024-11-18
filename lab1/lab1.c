#include <stdio.h>
#define MIN(A, B) (A < B ? A : B)

int main() {
    int a, b, c, x;
    printf("a = "); scanf("%i", &a);
    printf("b = "); scanf("%i", &b);
    printf("c = "); scanf("%i", &c);
    printf("x = "); scanf("%i", &x);
    int m = MIN(a, MIN(b, c));
    if(m <= x && m % 7 == 0) printf("case 1: %i\n", m);
    else {
        if(a+b+c-m == 0) {
            printf("сработала защита от дурака\n");
            return 1;
        }
        printf("case 2: %f\n", (float)m/(a+b+c-m));
    }
    return 0;
}
