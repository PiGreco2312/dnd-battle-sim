#include<stdio.h>
#include "LIST_characteristic.h"

LIST_CHARACTERISTIC NEW_LIST(){
  return NULL;
}

LIST_CHARACTERISTIC INSERT_feature(CHARACTERISTIC c, LIST_CHARACTERISTIC head) {
    LIST_CHARACTERISTIC new_node = malloc(sizeof(struct LIST_characteristic_node));
    
    if (new_node == NULL)
        return head; 

    new_node->characteristic=c;
    new_node->next= head;

    return new_node;
}

void PRINT_list(LIST_CHARACTERISTIC head){
  for (LIST_CHARACTERISTIC curr=head; curr!=NULL; curr=curr->next) {
    PRINT_feature(curr->characteristic);
  }
}

void READ_feature(CHARACTERISTIC feature){
  //FILE *fp=fopen("palle.txt", "r");
  //close(fp);
}