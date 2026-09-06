#ifndef _DICE_H
#define _DICE_H

struct dice{
    long quantity;
    long type;
    long modifier;
    long values[20];
};
typedef struct dice *DICE;

DICE NEW(void);
long roll(DICE, char *);
void converter(DICE, char *);
void sum_digits(char, long *, long);
void print_roll(DICE, long);

#endif