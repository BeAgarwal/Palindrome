''' Code by Shubham Agarwal
    Link: https://github.com/BeAgarwal/Palindrome '''

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

num = int(input("Enter the number: "))
ans = check_palindrome(num)
if ans:
    print(num, "is a palindrome.")
else:
    print(num, "is not a palindrome.")
