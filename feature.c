#include<stdio.h>
#include<stdlib.h>
#include"feature.h"

FEATURE NEW(){
    FEATURE f = (FEATURE)malloc(sizeof(struct feature));
    
    return f;
}