#include<class.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <LIST_feature.h>

#include <string.h>

class_name string_to_class(char *str) {
    if (strcmp(str, "ARTIFICER") == 0) return ARTIFICER;
    if (strcmp(str, "BARBARIAN") == 0) return BARBARIAN;
    if (strcmp(str, "BARD") == 0) return BARD;
    if (strcmp(str, "CLERIC") == 0) return CLERIC;
    if (strcmp(str, "FIGHTER") == 0) return DRUID;
    if (strcmp(str, "FIGHTER") == 0) return FIGHTER;
    if (strcmp(str, "ARTIFICER") == 0) return MONK;
    if (strcmp(str, "BARBARIAN") == 0) return PALADIN;
    if (strcmp(str, "BARD") == 0) return RANGER;
    if (strcmp(str, "CLERIC") == 0) return ROGUE;
    if (strcmp(str, "ARTIFICER") == 0) return SORCERER;
    if (strcmp(str, "BARBARIAN") == 0) return WARLOCK;
    if (strcmp(str, "BARD") == 0) return WIZARD;
    
    return ERR; 
}

void READ_class(char *filename) {
    FILE *file = fopen(filename, "r");    
    char buffer[1024]; 

    while (fgets(buffer, sizeof(buffer), file) != NULL) {
        buffer[strcspn(buffer, "\n")] = 0;
        char *class_name_str = strtok(buffer, "|");
        char *feature_name   = strtok(NULL, "|");
        char *description    = strtok(NULL, "|");
        char *uses_str       = strtok(NULL, "|");
        char *action_str     = strtok(NULL, "|");

        if (class_name_str && feature_name) 
            printf("Letta feature: %s per la classe %s\n", feature_name, class_name_str);
    }
    fclose(file);
}