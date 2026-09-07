#ifndef _MONSTER_H
#define _MONSTER_H
#include<stdio.h>
#include<stdlib.h>
#include<LIST_feature.h>

struct monster{
    char name[20];
    int cr;
    int ca;
    int exp;
    float speed;    //metres?
    LIST set_features;
};
typedef struct monster *MONSTER;

MONSTER NEW_monster(void);
#endif