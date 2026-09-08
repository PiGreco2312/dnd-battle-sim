#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include "dice.h"

DICE NEW(void) {
    DICE d = (DICE)malloc(sizeof(struct dice));
    if (d != NULL) {
        generate_id(d->id);
        d->quantity = 0;
        d->type = 0;
        d->modifier = 0;
        d->result=0;
    }
    return d;
}

void roll(DICE d, char *input){
    d->result=0;
    converter(d, input);
    
    for (int i=0; i<(d->quantity); i++){
        d->values[i]=rand() % d->type + 1;
        d->result+=(d->values[i]);
    }
}

void generate_id(char *id) { 
    int r;
    for (int i=0; i<DIM_ID; i++) {
         r = rand() % 62;
        
        if (r < 10) 
            id[i] = '0' + r;
            
        else if (r < 36)
            id[i] = 'A' + (r - 10);

        else 
            id[i] = 'a' + (r - 36);
    }

    id[DIM_ID] = '\0';
}

void converter(DICE d, char *input){
    char curr;
    long result=0, multp=1;

    for(int i=strlen(input)-1; i>=0; i--){
        curr=input[i];
        
        if(isdigit(curr)){
            sum_digits(curr, &result, multp);
            if(i==0)
                d->quantity=result;

            multp*=10;
        }else{
            if(i==0){
                if(curr=='a'){
                    //TODO later: advantage

                }else if(curr=='s'){
                    //TODO later: disadvantage
                }
            }else if(curr=='+')
                d->modifier=result;

            else if(curr=='-')
                d->modifier=-result;

            else if(curr=='d')
                d->type=result;

            result=0;
            multp=1;
        }
    }
}

void sum_digits(char curr, long *result, long multpl){
    *result+=(curr-'0')*multpl;
}

void print_roll(DICE d){
    printf("Result of dice %s(%ldd%ld+%ld): %ld\n", 
        d->id, d->quantity, d->type, d->modifier, d->result);

    printf("Values obtained: \n");
    for(int i=0; i<d->quantity; i++)
        printf("%ld\n", d->values[i]);
}