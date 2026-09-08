#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<time.h>
#include "dice.h"

//cd c:\Users\paolo\projects\dnd-battle-sim\folder_dice\
//gcc dice_test_main.c dice.c -o dice_test_main
//.\dice_test_main

int main(){
    srand(time(NULL));
    DICE d1, d2;
    for(int i=0; i<2; i++){
        printf("Dice 1:\n");
        d1=NEW();
        roll(d1, "8d6");
        print_roll(d1);
        printf("\n-----------------------------------------------------------------\n");
       
    }
}