#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <set>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */     int q;
    cin >> q;
    set <int> set_stl;
    while(q)
    {
        int instruction, val;
        cin >> instruction >> val;
        if(instruction == 1)
        {
            set_stl.insert(val);
        }
        else if (instruction == 2)
        {
            set_stl.erase(val);
        }
        else 
        {
           auto i =  set_stl.find(val);
           if(i != set_stl.end())
           {
               cout << "Yes" << endl;
           }
           else
           {
               cout << "No" << endl;
           }
        }
        q--;
    }
    return 0;
}



