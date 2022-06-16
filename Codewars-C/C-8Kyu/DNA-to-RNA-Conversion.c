// Link to kata : https://www.codewars.com/kata/5556282156230d0e5e000089

#include <stdlib.h>
#include <string.h>

char *dna_to_rna(const char *dna)
{
  int len = strlen(dna);
  char *temp = malloc(sizeof(dna)*len+1);
  strcpy(temp, dna);
  
  for (int i = 0; i < len; i++){
    if (temp[i] == 'T'){
      temp[i] = 'U';
    }
  }
  return temp;
}