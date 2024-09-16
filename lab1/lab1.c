#include <stdio.h>
#define MIN(A, B) (A < B ? A : B)
#define MAX(A, B) (A > B ? A : B)

int main() {
    float a, b, c, x;
    printf("a = "); scanf("%i", &a);
    printf("b = "); scanf("%i", &b);
    printf("c = "); scanf("%i", &c);
    printf("x = "); scanf("%i", &x);
    float m = MIN(a, MIN(b, c));
    if(m <= x && m % 7 == 0) printf("case 1: %i\n", m);
    else printf("case 2: %i\n", m/(a+b+c-m));
}
