#include "LIST_feature.h"

LIST_FEATURE NEW_LIST(){
  return NULL;
}

LIST_FEATURE INSERT_feature(FEATURE f, LIST_FEATURE head) {
    LIST_FEATURE new_node = malloc(sizeof(struct LIST_node));
    
    if (new_node == NULL)
        return head; 

    new_node->feature = f;
    new_node->next = head;

    return new_node;
}

void PRINT_list(LIST_FEATURE head){
  for (LIST_FEATURE curr=head; curr!=NULL; curr=curr->next) {
    PRINT_feature(curr->feature);
  }
}

void READ_feature(FEATURE feature){
  //FILE *fp=fopen("palle.txt", "r");
  //close(fp);
}