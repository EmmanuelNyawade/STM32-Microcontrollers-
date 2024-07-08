#include <stdio.h>

int main() {
    int rows, x, y, gap;
    // beginning of pyramid part of code

    printf("Enter number of required rows: ");
    scanf("%d", &rows);

    for (x = 1; x <= rows; x++) {
        // This prints the spaces in decreasing order
        for (gap = 1; gap <= rows - x; gap++) {
            printf(" ");
        }

        // This prints the asterisks in increasing order
        for (y = 1; y <= 2 * x - 1; y++) {
            printf("*");
        }

        printf("\n");
        
        //end of Pyramid part of code
    }
    //beginning of Diamond part of code
    
    printf("Enter number of required rows: ");
    scanf("%d", &rows);

    // Upper part of the diamond
    for (x = 1; x <= rows; x++) {
        // This prints the spaces in decreasing order
        for (gap = 1; gap <= rows - x; gap++) {
            printf(" ");
        }

        // This prints the asterisks in increasing order
        for (y = 1; y <= 2 * x - 1; y++) {
            printf("*");
        }

        printf("\n");
    }

    // Lower part of the diamond (excluding middle line if rows are odd)
    for (x = rows - 1; x >= 1; x--) {
        //This prints the spaces in increasing order
        for (gap = 1; gap <= rows - x; gap++) {
            printf(" ");
        }

        // This prins the asterisks in decreasing order
        for (y = 1; y <= 2 * x - 1; y++) {
            printf("*");
        }

        printf("\n");
    }
    
    //end of Diamond part of code



    return 0;
}
