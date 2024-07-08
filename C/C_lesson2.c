#include <stdio.h>
// single line comments
/* this is 
a multiple
line comments
*/


int main()
{
    int num1 = 30;
    int num2 = 66;
    int sum_numbers, diff_numbers, prod_numbers, mod_numbers;
    float quot_numbers;
    sum_numbers = num1 + num2;
    prod_numbers = num1 * num2;
    quot_numbers = num1 / num2;
    mod_numbers = num1 % num2;
    diff_numbers = num1 - num2;
    
    printf("The sum of %d and %d is %d \n", num1 , num2 , sum_numbers);
    printf("The product of %d and %d is %d \n", num1 , num2 , prod_numbers);
    printf("The quotient of %d and %d is %f \n", num1 , num2 , quot_numbers);
    printf("The modulus of %d and %d is %d \n", num1 , num2 , mod_numbers);
    printf("The difference of %d and %d is %d \n", num1 , num2 , diff_numbers);
    
    float x = 8;
    float y = 3;
    float z;
    z = x / y;
    printf("The quotient of %.4f and %.4f is %.4f", x ,y ,z);
    
    
    return 0;
}
