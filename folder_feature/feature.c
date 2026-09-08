#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include"feature.h"

FEATURE NEW_feature(void){
    FEATURE f=(FEATURE)malloc(sizeof(struct feature));
    if(f!=NULL) {
        strcpy(f->name, "");
        strcpy(f->desc, "");
        f->action=ACTION;
        f->saving_throw=0;
        f->number_uses=0;
    }
    return f;
}

FEATURE ADD_feature(char *n, char *d, int st, int uses, type_action a){
    FEATURE f=(FEATURE)malloc(sizeof(struct feature));
    if(f!=NULL) {
        strncpy(f->name, n, MAX_NAME-1);
        strncpy(f->desc, d, MAX_DESC-1);
        f->saving_throw=st;
        f->action=a;
        f->number_uses=uses;
    }
    return f;
}

void PRINT_feature(FEATURE f){
    printf("Feature:\n");
    printf("%s\n", f->name);
    printf("%s\n", f->desc);
    printf("%d\n", f->saving_throw);
    printf("%d\n", f->action);
}