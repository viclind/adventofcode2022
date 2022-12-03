#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int priority_value(int c)
{
    if (c > 90) 
    {
        return c - 96;
    }
    return c = c - 38;
}

int common_char(char *line, int size) 
{
    int i = 0, j = size - 1;
    int c;
    while (i < size / 2) {
        if (line[i] == line[j]) {
            c = line[i];
            break;
        }
        else if (j == size/2-1) {
            j = size - 1;
            i++;
        }
        else {
            j--;
        }
    }
    printf("Common char: %c\n", c);
    return priority_value(c);
}



int common_chars(char **lines, int *sizes) {
    int size = 1;
    char *commons = calloc(1, sizeof(char));
    int i = 0, j = 0;
    

    for (int i = 0; i < sizes[0]; i++) {
        for (int j = 0; j < sizes[1]; j++) {
            if (lines[0][i] == lines[1][j]) {
                commons[size] = lines[1][j];
                size++;
                commons = realloc(commons, size);
            }
        }
    }
    
    for (int i = 0; i < sizes[2]; i++) {
        for (int j = 0; j < size; j++) {
            if (lines[2][i] == commons[j]) {
                int val = commons[j];
                free(commons);
                return priority_value(val);
            }
        }
    }
    free(commons);
    return 0;
    
}

int main(void)
{
    FILE *fp;
    char *line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("i.txt", "r");

    char **lines = calloc(3, sizeof(char*));
    for (int i = 0; i < 3; i++) {
        lines[i] = (char*)malloc(100);
    }
    int *sizes = calloc(3, sizeof(int));

    int sum = 0;
    int i = 0;
    while ((read = getline(&line, &len, fp)) != -1) {
        strcpy(lines[i], line);
        sizes[i] = (int)read;
        if (i == 2) {
            i = 0;
            sum += common_chars(lines, sizes);
            continue;
        }
        i++;
        // sum += common_char(line, (int)read) #1
    }

    printf("SUM=%d\n", sum);

    fclose(fp);
    free(line);
    free(sizes);
    return 0;
}