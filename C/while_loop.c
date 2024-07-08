#include <stdio.h>

int main(){
    int iter , x , count;
    while (iter < 100){
        printf("Counting %d times \n", iter);
        iter +=2;
    }
    x = 20;
    while (count <10){
        printf("%d \n", x);
        x -= 2;
        count++;
        
    }
}