#ifndef _CLASS_H
#define _CLASS_H

struct clas{
    char name[20];
    
};
typedef struct clas *CLASS;

CLASS NEW(void);
#endif