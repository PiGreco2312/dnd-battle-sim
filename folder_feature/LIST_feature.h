#ifndef _LIST_FEATURE_H
#define _LIST_FEATURE_H
#include "feature.h"
/*
LISTA DI FEATURE 
*/
typedef struct LIST_feature_node *LIST_FEATURE;
struct LIST_feature_node{
    FEATURE feature;
    LIST_FEATURE next;
};


LIST_FEATURE NEW_list();
LIST_FEATURE INSERT_feature(FEATURE, LIST_FEATURE);
void PRINT_list(LIST_FEATURE);

#endif