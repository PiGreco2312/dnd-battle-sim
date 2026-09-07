#include<stdlib.h>
#include<string.h>
#include<stdio.h>
#include "dice.h"

int main(){
    DICE d=NEW();
    long result[100];
    result[0]=roll(d, "13d12+67");
    print_roll(d, result[0]);
    free(d);
}