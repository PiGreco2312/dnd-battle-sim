#ifndef _LIST_FEATURE_H
#define _LIST_FEATURE_H
#include<stdio.h>
#include<stdlib.h>
#include "feature.h"
/*
LISTA DI FEATURE 
*/

typedef struct LIST_node *LIST;

struct LIST_node{
    FEATURE feature;
    LIST next;
};

LIST NEW_list();
LIST INSERT_feature(FEATURE, LIST);
void PRINT_list(LIST);

#endif