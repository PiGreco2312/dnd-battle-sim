#ifndef _DICE_H
#define _DICE_H
#define DIM_ID 5
#define MAX_VALUES 50
struct dice{
    char id[DIM_ID];
    long quantity;
    long type;
    long modifier;
    long result;
    long values[MAX_VALUES];
};
typedef struct dice *DICE;

DICE NEW(void);
void generate_id(char *);
void roll(DICE, char *);
void converter(DICE, char *);
void sum_digits(char, long *, long);
void print_roll(DICE);

#endif