''' Code by Shubham Agarwal
    Link: https://github.com/BeAgarwal/Palindrome '''

'''Program to check whether the given floating point number is a palindrome or not.'''

def check_palindrome(n):
    n = remove_decimal(n)
    t = n
    r = 0
    while n > 0:
        rem = n % 10
        r = (r * 10) + rem
        n = n // 10
    if r == t:
        return True
    else:
        return False
        
def remove_decimal(n):
    s = str(n)
    s = s.replace('.','')
    print(s)
    return int(s)

num = float(input("Enter the floating number: "))
ans = check_palindrome(num)
if ans:
    print("Palindrome")
else:
    print("Not a palindrome")
    
