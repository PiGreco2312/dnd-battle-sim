#ifndef _FEAT_H
#define _FEAT_H
#include<LIST_feature.h>

struct feat{
    char name[20];
    int number_uses;
    LIST set_features;
};
typedef struct feat *FEAT;

FEAT NEW_feat();
#endif