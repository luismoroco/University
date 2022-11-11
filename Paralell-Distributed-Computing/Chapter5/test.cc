#include <bits/stdc++.h>
using namespace std;

int main(int, char**) {
  
  auto min_function = 
    [&] (volatile int64_t* c) -> void {
      int8_t r = 10;
      while (r--) 
        (*c)++;
  };
  
  int64_t c = 0; 

  std::cout << "ORGINAL: " << c << '\n';

  min_function(&c);

  std::cout << "REF: " << c << '\n';
}
