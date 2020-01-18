''' Code by Shubham Agarwal
    Link: https://github.com/BeAgarwal/Palindrome '''

def check_palindrome(s):
    s1=""
    for i in range(len(s)-1,-1,-1):
        s1 += s[i]
    if s1==s:
        return True
    else:
        return False
        
string = input("Enter the String.: ")
ans = check_palindrome(string)
if ans== True:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")
