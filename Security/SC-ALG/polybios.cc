#include <stdio.h>
#include <string.h>

const int N = 1 << 5;
char buffer[N];

int f(int p) {
  return p > 73 ? p - 66 : p - 65;
}

int main(int, char**) {
  char *mat = "ABCDEFGHIKLMNOPQRSTUVWXYZ", *index = "ABCDE";

  scanf("%s", &buffer);
  int len = strlen(buffer);

  // Cifrar 

  int i, j, x, y, d;
  char *cifr = new char[len * 2];
  for (d = 0, i = 0; i < len; ++i, d += 2) {
    j = f(buffer[i]);
    x = j / 5; y = j % 5;
    cifr[d] = index[x]; cifr[d+1] = index[y];
  }

  printf("CIFRADO = %s\n", cifr);

  // Descifrar

  char *desc = new char[len];
  for (d = 0, i = 0; d < len; i+=2, ++d) {
    x = f(cifr[i]); y = f(cifr[i+1]);
    desc[d] = mat[x * 5 + y];
  }

  printf("DESCIFRADO = %s\n", desc);

  delete[] cifr;
  delete[] desc;

  return 0;
}