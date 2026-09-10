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

type_action string_to_action(char *str) {
    str[strcspn(str, "\r\n")] = 0; 

    if (strcmp(str, "ACTION") == 0) return ACTION;
    if (strcmp(str, "BONUS_ACTION") == 0) return BONUS_ACTION;
    if (strcmp(str, "REACTION") == 0) return REACTION;
    if (strcmp(str, "PASSIVE") == 0) return PASSIVE; 
    
    return ERR; 
}

int find_savingthrow(char *desc) {
    if (desc == NULL) return 0;

    if (strstr(desc, "saving throw") != NULL ||
        strstr(desc, "Saving Throw") != NULL ||
        strstr(desc, "Saving throw") != NULL) {
        return 1; 
    }
    
    return 0; 
}

FEATURE READ_string_to_feature(char *buffer) {
    char *str_name  = strtok(NULL, "|");
    char *str_desc  = strtok(NULL, "|");
    int st = find_savingthrow(str_desc);
    char *str_uses  = strtok(NULL, "|");
    char *str_act   = strtok(NULL, "|");

    if (str_name) {
        int uses = atoi(str_uses);
        type_action act = string_to_action(str_act); 
        return ADD_feature(str_name, str_desc, st, uses, act);
    }
    
    return NULL; 
}