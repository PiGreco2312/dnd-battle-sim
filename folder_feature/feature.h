#ifndef _FEATURE_H
#define _FEATURE_H
#define MAX_NAME 50
#define MAX_DESC 200
/*
ADT GENERICO
*/

typedef enum{
    ACTION,         //0
    BONUS_ACTION,   //1
    REACTION        //2
}type_action;

struct feature{
    char name[MAX_NAME];
    char desc[MAX_DESC];
    int saving_throw;   //1: true, 0: false
    int number_uses;
    type_action action;
};
typedef struct feature *FEATURE;

FEATURE NEW_feature(void);
FEATURE ADD_feature(char *, char *, int, int, type_action);
void PRINT_feature(FEATURE);
void READ_feature(FEATURE);

#endif