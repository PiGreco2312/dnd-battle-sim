#ifndef _CLASS_H
#define _CLASS_H
#include<stdio.h>
#include<stdio.h>
#include<LIST_feature.h>
struct clas{
    char name[20];
    LIST set_features;
};
typedef struct clas *CLASS;

CLASS NEW_class();
#endif