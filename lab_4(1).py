#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
int main() {
char filename[] = "AILab.txt";
FILE *file = fopen("/Users/karishmavundavalli/Library/Mobile
Documents/com~apple~TextEdit/Documents/AILab.txt", "r");
if (file == NULL) {
perror("Error opening the file");
return 1;
}
int char_count = 0;
int num_count = 0;
int word_count = 0;
int in_word = 0;
int c;
while ((c = fgetc(file)) != EOF ) {
char_count++;
if (isdigit(c)) {
num_count++;
}
if (isspace(c) || ispunct(c)) {
in_word = 0;
} else if (!in_word) {
word_count++;
in_word = 1;
}
}
fclose(file);
printf("Number of characters: %d\n", char_count);
printf("Number of numbers: %d\n", num_count);
printf("Number of words: %d\n", word_count);
return 0;
}
