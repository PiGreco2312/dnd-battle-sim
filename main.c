#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<time.h>
#include "dice.h"

int main(){
    srand(time(NULL));
    DICE d1, d2;
    for(int i=0; i<2; i++){
        printf("Dice 1:\n");
        d1=NEW();
        roll(d1, "8d6");
        print_roll(d1);
        printf("\n-----------------------------------------------------------------\n");
        
        roll(d1, "8d6");
        print_roll(d1);
        free(d1);
        printf("\n-----------------------------------------------------------------\n");
        printf("\n-----------------------------------------------------------------\n");

        printf("Dice 2:\n");
        d2=NEW();
        roll(d2, "8d6");
        print_roll(d2);
        printf("\n-----------------------------------------------------------------\n");
        
        roll(d2, "8d6");
        print_roll(d2);
        free(d2);
        printf("\n-----------------------------------------------------------------\n");
        printf("\n-----------------------------------------------------------------\n");
    }
}