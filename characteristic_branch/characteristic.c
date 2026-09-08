#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include"characteristic.h"

CHARACTERISTIC NEW_characteristic(void){
    CHARACTERISTIC c=(CHARACTERISTIC)malloc(sizeof(struct characteristic));
    if(c!=NULL) {
        c->type=STRENGTH;
        c->value=0;
        c->modifier=0;
    }
    return c;
}

CHARACTERISTIC ADD_characteristic(char_type t, int val, int mod){
    CHARACTERISTIC c=(CHARACTERISTIC)malloc(sizeof(struct characteristic));
    if(c!=NULL) {
        c->type=t;
        c->value=val;
        c->modifier=mod;
    }
    return c;
}

void PRINT_characteristic(CHARACTERISTIC c){
    printf("Characteristic:\n");
    printf("%d\n", c->type);
    printf("%d\n", c->value);
    printf("%d\n", c->modifier);
}

void READ_characteristic(CHARACTERISTIC){

}
