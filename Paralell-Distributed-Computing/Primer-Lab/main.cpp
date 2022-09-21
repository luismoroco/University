#include <iostream>
#include <ctime>
#include <fstream>

const int MAX = 10000;

bool A[MAX][MAX], x[MAX], y[MAX];
double time__;

int main() {

    std::ofstream outFile;
    outFile.open("out.txt");

    std::clock_t start, end;
    int i, j;

    for (i = 0; i < MAX; ++i) {
        for (j = 0; j < MAX; ++j) {
            A[i][j] = 1;
        }
        x[i] = 1;
    }
    
    for (int k = 1000; k <= 10000; k+=1000) {
        
        //std::cout << "TEST: " << k << '\n';

        start = clock();
        for (i = 0; i < k; ++i) 
            for (j = 0; j < k; ++j)
                y[i] += A[i][j] * x[j];
        end = clock();

        time__ = double(end - start)/CLOCKS_PER_SEC;
        //std::cout << "TIME LOOP 1: " << time__ << '\n';

       
        start = clock();
        for (j = 0; j < k; ++j) 
            for (i = 0; i < k; ++i)
                y[i] += A[i][j] * x[j];
        end = clock();

        auto time_ = double(end - start)/CLOCKS_PER_SEC;
        //std::cout << "TIME LOOP 2: " << time__ << '\n';

        outFile << k << ' ' << time__ << ' ' << time_ << '\n';

    }

    outFile.close();
    
    return 0;
}