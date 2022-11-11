#include <bits/stdc++.h>
using namespace std;

constexpr int N = 1 << 5;
int r, c, i, j;

int main(int, char**) {
  string b;
  getline(cin, b);

  // white space 

  for (int i = 0; i < b.length(); ++i) {
    if (b[i] == ' ') 
      b.erase(i, 1);
  }

  // Upp

  while (b.find("ñ") != string::npos) {
    auto i = b.find("ñ");
    b.erase(i, 2);
    b.insert(i, "*");
  }

  for (int i = 0; i < b.length(); ++i)
    b[i] = (b[i] == '*') ? 'n' : b[i];

  char *buffer = new char[b.length()];
  for (int i = 0; i < b.length(); ++i)
    buffer[i] = toupper(b[i]);
  

  // replace

  for (int i = 0; i < b.length(); ++i)
    buffer[i] = b[i];
  

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

  printf("\n");

  return 0;
}