#ifndef _PG_H
#define _PG_H
#include<LIST_feature.h>
struct pg{
    char name[20];
    int level;
    int armour_class;
    int proficiency_bonus;
    float speed;    //metres?
    //CHARACTERISTIC ;
    LIST set_features;
};
typedef struct pg *PG;

PG NEW_pg();
#endif