#ifndef _CHARACTERISTIC_H
#define _CHARACTERISTIC_H

typedef enum {
    STRENGTH,
    DEXTERITY,
    CONSTITUTION,
    INTELLIGENCE, 
    WISDOM,
    CHARISMA
} char_type;

struct characteristic{
    char_type type;
    int value;
    int modifier;
};
typedef struct characteristic *CHARACTERISTIC;

CHARACTERISTIC NEW_characteristic(void);
CHARACTERISTIC ADD_characteristic(char_type, int, int);
void PRINT_characteristic(CHARACTERISTIC);
void READ_characteristic(CHARACTERISTIC);

#endif