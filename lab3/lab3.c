#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void fill(int n, int a[]) {
    for (int i = 0; i < n; ++i)
        a[i] = rand() % 101 - 50;
}

int compute(int n, int A[n]) {
    /* Найдём 3 максимума и их индексы */
    int M[3] = {0}, I[3];
    for(int i = 0; i < n; ++i) {
        if(A[i] > *M) {
            *M = A[i];
            *I = i;
        }
    }
    for(int i = 0; i < n; ++i) {
        if(i == *I) {
            ++i;
            if(i >= n) break;
        }
        if(A[i] > 1[M]) {
            *(1+M) = A[i];
            1[I] = i;
        }
    }
    for(int i = 0; i < n; ++i) {
        if(i == *I || i == *(1+I)) {
            ++i;
            if(i >= n) break;
        }
        if(i[A] > 2[M]) {
            *(2+M) = A[i];
            2[I] = i;
        }
    }
    return *M*1[M]*2[M] - ((*I+1[I]+2[I]) % n);
}

int main() {
    srand(time(NULL));
    int n;
    printf("n -> ");
    scanf("%d", &n);
    int A[n];
    fill(n, A);

    printf("%i\n", compute(n, A));
    return 0;
}
