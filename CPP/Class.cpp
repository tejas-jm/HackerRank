#include <iostream>
#include <sstream>
using namespace std;

/*
Enter code for class Student here.
Read statement for specification.
*/
class Student { 
    public : 
       int age;
       string First_Name;
       string Last_Name;
       int Standard; };

int main(){
    
     Student candidate; 
     cin>>candidate.age; 
     cin>>candidate.First_Name; 
     cin>>candidate.Last_Name; 
     cin>>candidate.Standard;

    cout<<candidate.age<<endl;
    cout<<candidate.Last_Name<<", "<<candidate.First_Name<<endl;
    cout<<candidate.Standard<<endl;
    cout<<endl;

    cout<<candidate.age<<","<<candidate.First_Name<<","<<candidate.Last_Name<<","<<candidate.Standard<<endl;;

return 0;
}


