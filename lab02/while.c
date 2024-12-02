#include <stdio.h>
#include <math.h>

float f(float x, float h) {
    const float eps = h/2;
    if(x > 0.0f - eps && x <= 1.1f + eps)
      return cos(x)*exp(sqrt(pow(-x,2)));
    else if(x >= 1 - eps && x <= 2 + eps)
      return log(x+1)-sqrt(4-pow(x,2));
    return 0.0f;
}

int main() {
    float h, x = 0;
    printf("введите h> "); scanf("%f", &h);
    printf("x\t\tf(x)\n");
    while(x <= 2.0f) {
        printf("%f\t%f\n", x+h, f(x, h));
        x += h;
    }
    return 0;
}
