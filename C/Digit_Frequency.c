#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>


int main() {

    /* Enter your code here. Read input from STDIN. Print output to STDOUT */     
    char arr[1000];
    scanf("%s",arr);
    int n = strlen(arr);
    
    
    int count[10] = {0};
    
    // printf("%s\n",arr);
    
    for(int i = 0; i < n; i++)
    {
        // printf("%c\n",arr[i]);
    int temp  = (int)(arr[i]) - 48;
       if (temp >= 0 && temp <= 9)
       {
           count[temp] += 1;
        //    printf("%d",arr[i]);
       } 
    }
    
    for (int i = 0; i < 10; i++)
    {
        printf("%d ", count[i]);
    }
     
    return 0;
}
 
