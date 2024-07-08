
#include <stdio.h>

int main()
{
    char gender = ' ';
    int weight;
    float distance;
    printf("Enter your gender: \n");
    scanf( "%c", &gender);
    printf("My gender is %c", gender);
    printf("\n");
    
    printf("Enter your weight: \n");
    scanf( "%d", &weight);
    printf("My weight is %d kgs", weight);
    printf("\n");
    
    printf("Enter your distance: \n");
    scanf( "%f", &distance);
    printf("My distance covered is %.2f metres", distance);



  
    
 
    return 0;
}