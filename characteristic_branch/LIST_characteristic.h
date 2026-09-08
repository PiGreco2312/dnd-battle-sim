#ifndef _LIST_CHARACTERISTIC_H
#define _LIST_CHARACTERISTIC_H
#include "characteristic.h"

struct LIST_characteristic_node{
    CHARACTERISTIC characteristic;
    LIST_CHARACTERISTIC next;
};
typedef struct LIST_characteristic_node *LIST_CHARACTERISTIC;

LIST_CHARACTERISTIC NEW_list();
LIST_CHARACTERISTIC INSERT_characteristic(CHARACTERISTIC, LIST_CHARACTERISTIC);
void PRINT_list(LIST_CHARACTERISTIC);

#endif