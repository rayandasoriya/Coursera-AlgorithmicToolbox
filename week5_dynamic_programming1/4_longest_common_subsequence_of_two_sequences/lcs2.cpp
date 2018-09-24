#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include<bits/stdc++.h>

using std::vector;
using std::string;

int max(int a, int b);

int lcs2L(vector<int> &a, vector<int> &b) {
    int Asize = a.size();
    int Bsize = b.size();
    int D[Asize+1][Bsize+1];
    
    for(int i=0; i<=Asize; i++) {
        for(int j=0; j<=Bsize; j++) {
            if(i == 0 || j == 0)
                D[i][j] = 0;
            else if(a[i-1] == b[j-1])
                D[i][j] = D[i-1][j-1] + 1;
            else
                D[i][j] = std::max(D[i-1][j],D[i][j-1]);
        }
    }
    return D[Asize][Bsize];
}
int main() {
    size_t n;
    std::cin >> n;
    vector<int> a(n);
    for (size_t i = 0; i < n; i++) {
        std::cin >> a[i];
    }
    
    size_t m;
    std::cin >> m;
    vector<int> b(m);
    for (size_t i = 0; i < m; i++) {
        std::cin >> b[i];
    }
    
    std::cout << lcs2L(a, b) << std::endl;
    
    
}
