#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * Complete the 'insertionSort1' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY arr
 */

 // Function to perform one iteration of insertion sort

void insertionSort1(int n, vector<int> arr) {
     
    int ele = arr[n-1]; // Get the last element as the element to be inserted
    for (int i = 0; i < n; i++) {
        int temp = ele; // Store the element temporarily
        if (arr[n - i - 2] > temp) {
            arr[n - i - 1] = arr[n - i - 2]; // Shift elements to the right if they are greater than the element
        } else {
            arr[n - i - 1] = temp; // Insert the element at the correct position
            break;
        }
        // Print the current state of the array after each iteration
        for (auto i : arr) {
            cout << i << " ";
        }
        cout << endl;
    }
    // Print the final sorted array
    for (auto i : arr) {
        cout << i << " ";
    }
    cout << endl;
}



int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split(rtrim(arr_temp_temp));

    vector<int> arr(n);

    for (int i = 0; i < n; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    insertionSort1(n, arr);

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
