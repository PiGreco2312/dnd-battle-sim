#ifndef _FEATURE_H
#define _FEATURE_H
#define MAX_NAME 50
#define MAX_DESC 200

typedef enum{
    ACTION,         //0
    BONUS_ACTION,   //1
    REACTION,       //2
    PASSIVE,        //3
    ERR             //4
}type_action;

struct feature{
    char name[MAX_NAME];
    char desc[MAX_DESC];
    int saving_throw;   //1: true, 0: false
    int number_uses;
    type_action action;
};
typedef struct feature *FEATURE;

type_action string_to_action(char *);
int find_savingthrow(char *);
FEATURE READ_string_to_feature();
FEATURE NEW_feature(void);
FEATURE ADD_feature(char *, char *, int, int, type_action);
void PRINT_feature(FEATURE);

#endif