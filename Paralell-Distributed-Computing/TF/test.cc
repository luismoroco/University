#include <iostream>
#include <memory>

constexpr int64_t N = 10;

class WidgetMemoryMaker {
  private: 
    std::unique_ptr<int[]> data;
  public:
    WidgetMemoryMaker(const int size): 
      data(std::make_unique<int[]>(size)) {}

    void do_something() {}
};

void useWidgetMaker() {
  WidgetMemoryMaker w(10);

  w.do_something();
} 

#include <stdio.h>
#include<stdlib.h>

int main(int, char**) {
  int* ptr = (int*) malloc(5 * sizeof(int));

  free(ptr);

  

  return 0;
}
