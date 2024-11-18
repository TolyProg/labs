#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// что называется "tagged union"
typedef struct Data {
    enum {INT, FLOAT, DOUBLE, VOIDP} tag; // и т.д.
    union {
        int i; float f; double d; void *voidp;
    } d; // тоже можно добавить значений
    // кстати, остальные значения можно писать/читать,
    // даже не имея для них специального тега путём
    // кастования указателя на пустоту
} Data;

// однонаправленный список
typedef struct List {
    Data data;
    struct List *next;
} List;

// не очень эффективно, но это же просто лаба :)
void list_append(List *l, const Data d) {
    while(l->next != NULL)
        l = l->next;
    l = malloc(sizeof(List));
    *l = (List){d, NULL};
}

Data list_get(List *l, int i) {
    // если будет передан out-of-bounds индекс, то программа вылетит
    while(i-- > 0)
        l = l->next;
    return l->data;
}

void fill(int n, List *l) {
    for (int i = 0; i < n; ++i) {
        l->next = malloc(sizeof(List));
        *l->next = (List){(Data){.tag=INT, .d.i=rand() % 101 - 50}};
        l = l->next;
    }
    l->next = NULL;
}

int compute(int n, List *l) {
    /* Найдём 3 максимума и их индексы */
    int M[3] = {0}, I[3];
    List *p = l;
    for(int i = 0; i < n; ++i) {
        if(p->data.d.i > *M) {
            *M = p->data.d.i;
            *I = i;
        }
        l = l->next;
    }
    p = l;
    for(int i = 0; i < n; ++i) {
        if(i == *I) {
            ++i;
            if(i >= n) break;
        }
        if(p->data.d.i > 1[M]) {
            *(1+M) = p->data.d.i;
            1[I] = i;
        }
    }
    p = l;
    for(int i = 0; i < n; ++i) {
        if(i == *I || i == *(1+I)) {
            ++i;
            if(i >= n) break;
        }
        if(p->data.d.i > 2[M]) {
            *(2+M) = p->data.d.i;
            2[I] = i;
        }
    }
    return *M*1[M]*2[M] - ((*I+1[I]+2[I]) % n);
}

int main() {
    srand(time(NULL));
    List l; // выделяю на стеке (эффективнее, чем malloc)
    int n;
    printf("n -> ");
    scanf("%d", &n);
    fill(n, &l);

    printf("%i\n", compute(n, &l));
    return 0;
}
