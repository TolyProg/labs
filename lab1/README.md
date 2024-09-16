# Лабораторная работа №1

## Вариант 3
Вывести значение наименьшего из трёх параметров $a$, $b$, $c$ если оно меньше или равно $x$ и кратно 7, и частное наименьшего параметра и суммы двух оставшихся иначе.

## Блок-схема
TODO


## Программа
```c
#include <stdio.h>
#define MIN(A, B) (A < B ? A : B)
#define MAX(A, B) (A > B ? A : B)

int main() {
    float a, b, c, x;
    printf("a = "); scanf("%f", &a);
    printf("b = "); scanf("%f", &b);
    printf("c = "); scanf("%f", &c);
    printf("x = "); scanf("%f", &x);
    float m = MIN(a, MIN(b, c));
    if(m <= x && m % 7 == 0) printf("case 1: %f\n", m);
    else printf("case 2: %f\n", m/(a+b+c-m));
    return 0;
}
```

## Переработанная программа из примера
```c
#include <stdio.h>

int main() {
    float a, b, c;
    printf("Enter a -> "); scanf("%f", &a);
    printf("Enter b -> "); scanf("%f", &b);
    printf("Enter c -> "); scanf("%f", &c);
    float x = 1.0f;
    if(!a && !b && !c) return 0;
    printf("f(x) =");
    if(a) printf(" %fx^2", a);
    if(b) {
        if(b < 0.0f) printf(" - %fx", -b);
        else printf(" + %fx", b);
    }
    if(c) {
        if(
```
