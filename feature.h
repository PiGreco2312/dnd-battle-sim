#ifndef _FEATURE_H
#define _FEATURE_H
#define MAX_NAME 50
#define MAX_DESC 200
/*
LISTA DI FEATURE 
ADT GENERICO
*/

typedef enum{
    ACTION,
    BONUS_ACTION,
    REACTION
}action_type;

struct feature{
    char name[MAX_NAME];
    char desc[MAX_DESC];
    action_type action;
    int saving_throw;   //1: true, 0: false

    FEATURE feature_next;
};
typedef struct feature *FEATURE;

FEATURE NEW_FEATURE(void);

#endif