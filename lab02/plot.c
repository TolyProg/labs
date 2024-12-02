#include <stdio.h>
#include <math.h>
#include <raylib.h>

float f(float x, float h) {
    const float eps = h/2;
    if(x > 0.0f - eps && x <= 1.1f + eps)
        return cos(x)*exp(sqrt(pow(-x,2)));
    else if(x >= 1 - eps && x <= 2 + eps)
        return log(x+1)-sqrt(4-pow(x,2));
    return 0.0f;
}


#define W 400
#define H 320

#define OX 100
#define OY H-120
#define SCALE 100

int main() {
    InitWindow(W, H, "plot.c");
    float h;
    //printf("введите h> "); scanf("%f", &h);
    h = 0.1;
    printf("x\t\tf(x)\n");
    //for(float x = 0; x <= 2.0f; x += h)
    //    printf("%f\t%f\n", x+h, f(x, h));
    SetTargetFPS(30);
    while(!WindowShouldClose()) {
        BeginDrawing();
        ClearBackground(RAYWHITE);
        int prevX = 0, prevY = f(0, h)*SCALE;
        for(float x = 0+h; x <= 2.0f; x += h) {
            int tX = x*SCALE;
            int tY = f(x, h)*SCALE;
            DrawLine(OX+prevX, OY-prevY, OX+tX, OY-tY, RED);
            prevX = tX;
            prevY = tY;
        }
        EndDrawing();
    }
    CloseWindow();
    return 0;
}
