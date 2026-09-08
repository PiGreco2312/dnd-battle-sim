#ifndef _SPELL_H
#define _SPELL_H
#define MAX_DIM 100
#include<LIST_feature.h>

typedef struct timing{
    int concentration;
    int amount;
    char time_unit[MAX_DIM];
};

struct spell{
    char name[MAX_DIM];
    char school[MAX_DIM];
    int level;

    action_type casting_time;
    char components[MAX_DIM];
    timing duration; 
    int range;  //-1: self    -   0: touch
    
    char description[MAX_DIM];

    int is_damage;
    char damage[MAX_DIM];
    int is_heal;
    char heal[MAX_DIM];
    int is_buff;
    char buff[MAX_DIM];

    int is_upcast;
};
typedef struct spell *SPELL;

SPELL NEW_spell();
#endif