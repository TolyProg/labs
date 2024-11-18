#include <stdio.h>
#include <stdlib.h>
#define MIN(A, B) (A < B ? A : B)

void durak() {
    printf("сработала защита от дурака\n");
    exit(1);
}

void w(int r) {
    if(r <= 0) durak();
}

int main() {
    int a, b, c, x;
    printf("a = "); w(scanf("%i", &a));
    printf("b = "); w(scanf("%i", &b));
    printf("c = "); w(scanf("%i", &c));
    printf("x = "); w(scanf("%i", &x));
    int m = MIN(a, MIN(b, c));
    if(m <= x && m % 7 == 0) printf("case 1: %i\n", m);
    else {
        if(a+b+c-m == 0) durak();
        printf("case 2: %f\n", (float)m/(a+b+c-m));
    }
    return 0;
}
