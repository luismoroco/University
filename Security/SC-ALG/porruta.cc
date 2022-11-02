#include <iostream>
#include <stdio.h>
#include <string.h>

const int N = 1 << 5;
char buffer[N];
int r, c, i, j;

int main(int, char**) {
  scanf("%s", &buffer);

  scanf("%d %d", &r, &c);
  int pr = r, pc = c;

  char cif[r][c];
  memset(cif, -1, sizeof(cif));

  // Cifrar 

  char *ptr = buffer; 
  while (r-- && *ptr) {
    if ((r % 2) == 0) 
      for (i = 0; i < c; ++i) 
        cif[r][i] = *ptr ? *ptr++ : -1;
    else 
      for (i = c - 1; i >= 0; --i)
        cif[r][i] = *ptr ? *ptr++ : -1;
  }

  printf("CIFRADO\n");
  for (i = 0; i < pr; ++i) {
    for (j = 0; j < pc; ++j) 
      printf("%c\t", cif[i][j]);
    printf("\n");
  }

  // Descifrar 

  printf("DESCIFRADO\n");
  while (pr--) {
    if ((pr % 2) == 0) 
      for (i = 0; i < c; ++i) 
        printf("%c", cif[pr][i]);
    else 
      for (i = c - 1; i >= 0; --i)
        printf("%c", cif[pr][i]);
  }

  return 0;
}