import java.io.*;
import java.util.*;


  
public class Solution {

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        String A=sc.next();
        String B=sc.next();
        sc.close();
        /* Enter your code here. Print output to STDOUT. */
        int n = A.length() + B.length();
        System.out.println(n);
        if (A.compareTo(B) > 0)
        {
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
        A = A.substring(0,1).toUpperCase() + A.substring(1);
        B = B.substring(0,1).toUpperCase() + B.substring(1);
        System.out.println(A + " " + B);      
      
    }
}



