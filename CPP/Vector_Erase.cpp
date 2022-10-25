#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */     vector <int> v;
    int n;
    cin >> n;
    int a;
    for(int i = 0; i < n; i++)
    {
        cin >> a;
        v.push_back(a);
    }
    int pos, lower_bound, upper_bound;
    cin >> pos;
    // cout << pos << endl;
    cin >> lower_bound >> upper_bound;
    // cout << lower_bound << " " << upper_bound << endl;
    v.erase(v.begin() + pos - 1);
    v.erase(v.begin() + lower_bound - 1, v.begin() + upper_bound - 1);
    cout << v.size() << endl;
    for (int j = 0; j < v.size() ; j++)
    {
        cout << v.at(j) << " ";
    }
    return 0;
    
}
