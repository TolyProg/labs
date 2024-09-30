#include <stdio.h>
#include <math.h>

float f(float x) {
    return 0 <= x && x <= 1 ?
      cos(x)*exp(sqrt(pow(-x,2))) :
      log(x+1)-sqrt(4-pow(x,2));
}

int main() {
    float h;
    printf("введите h> "); scanf("%f", &h);
    printf("x\t\tf(x)\n");
    for(float x = 0; x <= 1.0f; x += h)
        printf("%f\t%f\n", x+h, f(x));
    return 0;
}
