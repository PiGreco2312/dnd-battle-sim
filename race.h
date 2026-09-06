#ifndef _RACE_H
#define _RACE_H

struct race{
    char name[20];
    
};
typedef struct race *RACE;

RACE NEW(void);
#endif