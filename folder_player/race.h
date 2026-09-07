#ifndef _RACE_H
#define _RACE_H
#include<stdio.h>
#include<stdio.h>
#include<LIST_feature.h>

struct race{
    char name[20];
    LIST set_feature;
};
typedef struct race *RACE;

RACE NEW_race(void);
#endif