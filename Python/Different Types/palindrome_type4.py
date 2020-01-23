''' Code by Shubham Agarwal
    Link: https://github.com/BeAgarwal/Palindrome '''

'''Program to find Sum of all N digit palindrome numbers.'''

def check_palindrome(n):
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

d = int(input("Enter the digit: "))
rangefrom = pow(10, (d - 1))
rangeto = pow(10, d) - 1

S = 0
c = 0
for i in range(rangefrom, rangeto):
    ans = check_palindrome(i)
    if ans:
        c = c + 1
        S = S + i
print("There are", c,"palindrome numbers of", d, "digits.")
print("Sum of", d ,"digit palindrome numbers is:", S)


'''OUTPUT
Enter the digit: 4
There are 89 palindrome numbers of 4 digits.
Sum of 4 digit palindrome numbers is: 485001
'''
