#ifndef _CLASS_H
#define _CLASS_H
#include <LIST_feature.h>

typedef enum{
    ARTIFICER,
    BARBARIAN,
    BARD,
    CLERIC,
    DRUID,
    FIGHTER,
    MONK,
    PALADIN,
    RANGER,
    ROGUE,
    SORCERER,
    WARLOCK,
    WIZARD,
    ERR
}class_name;

struct clas{
    class_name name;
    LIST_FEATURE set_features;
};
typedef struct clas *CLASS;

class_name string_to_class(char *);
void READ_class(char *);

#endif