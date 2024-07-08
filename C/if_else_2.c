#include <stdio.h>

int main(){
    int salary;
    printf("Enter your monthly salary: ");
    scanf("%d", &salary);
    printf("Your old salary is %d" , salary);
    printf("\n");
    
    if (salary < 50000){
        salary *= 1.1;
    }
    else if ( salary >= 50000 && salary < 80000){
        salary *= 1.05;
    }
    else {
        salary *= 0.95;
    }
    printf("Your new salary is %d ", salary);
    

    return 0;
}