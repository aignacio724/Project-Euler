#include <stdio.h>

int main()
{
    int sum = 0;
    int i;

    for (i = 0; i < 1000; i++) {

        printf("i: %d ", i);
        if (i % 3 == 0 || i % 5 == 0) {
            sum += i;
            printf("Found multiple! sum: %d", sum);
        }
        printf("\n");
    }

    printf("Sum of the multiples of 3 or 5: %d\n", sum);
}    
