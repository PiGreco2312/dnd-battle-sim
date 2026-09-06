#include<stdlib.h>
#include<stdio.h>
#include <string.h>
#include <ctype.h>
#include <time.h>
#include "dice.h"

DICE NEW(void) {
    DICE d = (DICE)malloc(sizeof(struct dice));
    if (d != NULL) {
        d->quantity = 0;
        d->type = 0;
        d->modifier = 0;
    }
    return d;
}

long roll(DICE d, char *input){
    long tot=0;
    converter(d, input);
    long result[d->quantity];
    srand(time(NULL));
    
    for (int i=0; i<(d->quantity); i++){
        result[i]=rand() % d->type + 1;
        d->values[i]=result[i];
        tot+=result[i];
    }
    return tot+d->modifier;
}

void converter(DICE d, char *input){
    char curr;
    long result=0, multp=1;
    d->modifier=0;
    d->type=0;
    d->quantity=0;

    for(int i=strlen(input)-1; i>=0; i--){
        curr=input[i];
        
        if(isdigit(curr)){
            sum_digits(curr, &result, multp);
            if(i==0)
                d->quantity=result;

            multp*=10;
        }else{
            if(curr=='+'){
                d->modifier=result;

            }else if(curr=='-'){
                d->modifier=-result;

            }else if(curr=='d'){
                d->type=result;

            }
            result=0;
            multp=1;
        }
    }
}

void sum_digits(char curr, long *result, long multpl){
    *result+=(curr-'0')*multpl;
}

void print_roll(DICE d, long result){
    printf("Result of %ldd%ld+%ld: %ld\n", d->quantity, d->type, d->modifier, result);
    printf("Values obtained: \n");
    for(int i=0; i<d->quantity; i++){
        printf("%ld\n", d->values[i]);
    }
}