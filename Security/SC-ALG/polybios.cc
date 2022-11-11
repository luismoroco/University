#include <bits/stdc++.h>
using namespace std;

constexpr int N = 1 << 10;

int f(int p) {
  return p > 73 ? 
    p - 66 : p - 65;
}

int main(int, char**) {
  char *mat = "ABCDEFGHIKLMNOPQRSTUVWXYZ", *index = "ABCDE";

  string buffer; 
  getline(cin, buffer);

  int len = buffer.size();

  cout << "CIF: " << buffer << '\n';

  // Vars
  int i, j, x, y, d;
  
  // Mayus

  for (i = 0; i < len; ++i) 
    buffer[i] = toupper(buffer[i]);

  cout << "CIF: " << buffer << '\n';

  // Cifrar 

  char *cifr = new char[len * 2];
  for (d = 0, i = 0; i < len; ++i, d += 2) {
    j = f(buffer[i]);
    x = j / 5; y = j % 5;
    cifr[d] = index[x]; cifr[d+1] = index[y];
  }

  cout << "CIFRADO: " << cifr << '\n';

  // Descifrar

  char *desc = new char[len];
  for (d = 0, i = 0; d < len; i+=2, ++d) {
    x = f(cifr[i]); y = f(cifr[i+1]);
    desc[d] = mat[x * 5 + y];
  }

  cout << "DESCIFRADO: " << desc << '\n';

  delete[] cifr;
  delete[] desc;

  return 0;
}
