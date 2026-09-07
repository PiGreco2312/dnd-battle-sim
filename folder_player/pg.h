#ifndef _PG_H
#define _PG_H
#include<feature.h>

struct pg{
    char name[20];
    int level;
    FEATURE features[];
};
typedef struct pg *PG;

PG NEW_PG(void);
#endif