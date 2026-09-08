#ifndef _LIST_FEATURE_H
#define _LIST_FEATURE_H
#include<stdio.h>
#include<stdlib.h>
#include "feature.h"
/*
LISTA DI FEATURE 
*/
struct LIST_node{
    FEATURE feature;
    LIST_FEATURE next;
};
typedef struct LIST_node *LIST_FEATURE;

LIST_FEATURE NEW_list();
LIST_FEATURE INSERT_feature(FEATURE, LIST_FEATURE);
void PRINT_list(LIST_FEATURE);

#endif