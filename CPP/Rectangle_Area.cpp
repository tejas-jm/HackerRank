#include <iostream>

using namespace std;

class Rectangle {
    
    public: 
        int l, b;
        void display() {
            cout << l << " " << b << endl;
        }
};

class RectangleArea:public Rectangle {
    
    public:
        void read_input() {
            cin >> l >> b;
        }
        
        void display() {
            int area = l*b;
            cout << area;
        }
};

int main()
{
    
     //Declaring a RectangleArea object
     
    RectangleArea r_area;
    
   
    // Reading the width and height
     
    r_area.read_input();
    
    
     //Printing the width and height
     
    r_area.Rectangle::display();
    
    /*
     * Print the area
     */
    r_area.display();
    
    return 0;
}
