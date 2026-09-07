#ifndef _PG_H
#define _PG_H
#include<stdio.h>
#include<stdlib.h>
#include<LIST_feature.h>
struct pg{
    char name[20];
    int level;
    int ca;
    float speed;    //metres?
    LIST set_features;
};
typedef struct pg *PG;

PG NEW_pg(void);
#endif