#include <stdio.h>
int main(){
    char country[50] = {"Kenya", "Rwanda", "Russia", "Australia", "Japan"}
    printf("Enter your Country: ");
    scanf("%s" , country);
    
    switch(country[]){
        case 0:
            printf("Your capital city is Nairobi.");
            break;
        case 1:
            printf("Your capital city is Kigali.");
            break;
        case 2:
            printf("Your capital city is Moscow.");
            break;
        case 3:
            printf("Your capital city is Sydney.");
            break;
        case 4:
            printf("Your capital city is Tokyo.");
            break;
        default:
            printf("Invalid Country.")
    }

    
    return 0;
    
}