''' Code by Shubham Agarwal
    Link: https://github.com/BeAgarwal/Palindrome '''

'''Program to check the sum of a digit is a palindrome or not.'''
    
def check_palindrome(n):
    r = 0
    t = n
    while n > 0:
        rem = n % 10
        r = (r * 10) + rem
        n = n // 10
    if r == t:
        return True
    else:
        return False

def sumfunc(n):
    s = 0
    while n > 0:
        rem = n % 10
        s = s + rem
        n //= 10
    print("Sum of a digit is:", s)
    return check_palindrome(s)
    
num = int(input("Enter the number: "))
ans = sumfunc(num)
if ans:
    print("Palindrome.")
else:
    print("Not a Palindrome.")
