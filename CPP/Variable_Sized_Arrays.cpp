#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */     vector <int> v;
    int var_arr_1, var_arr_2;
    cin >> var_arr_1 >> var_arr_2;
    vector <vector<int>> vec;
    while(var_arr_1)
    {
        int nested_vec_size {0};
        cin >> nested_vec_size;
        vector <int> v;
        int val {0};
        for(int i = 0; i < nested_vec_size; i++)
        {
            cin >> val;
            v.push_back(val);
        }
        vec.push_back(v);
        var_arr_1--;
    }
    while(var_arr_2)
    {
        int index, nested_index;
        cin >> index >> nested_index;
        int ans = vec.at(index).at(nested_index);
        cout << ans << endl;
        var_arr_2--;
    }
    return 0;
}
