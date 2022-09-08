import math

def is_smart_number(num):
    val = int(math.sqrt(num))
    if num == val*val:
        return True
    return False

for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")



# For anyone wondering if there's some kind of secret mathematical theory law that calculates how many factors something has based on whether it has a 
# square root: technically yes, technically no. The reasoning behind it is... a number normally has two factors. A larger one and a smaller one. 
# The only time the numbers will not be different is if it's the same factors (which sounds obvious when written out, but not when you're trying 
# to figure out how you can have odd numbers). And the only time you can have a pair of factors that are the same is if it's a squareable number.
# The square is the odd factor. So like (a,b,c,b,a). It doesn't matter if it has other factors. If it doesn't, then you just have the values 1, 
# the square root, and the number itself. Otherwise, it's like (1,a,b,c,d (the square root),[num/c],[num/b],[num/a],num). Hope this makes sense.
