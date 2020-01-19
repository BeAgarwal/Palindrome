''' Code by Shubham Agarwal
    Link: https://github.com/BeAgarwal/Palindrome '''

def recursive_str(s):
    if len(s)==0:
        return s
    else:
        return recursive_str(s[1:])+s[0]
string = input("Enter the String: ")
ans = recursive_str(string)
if ans== string:
    print(string, "is a palindrome.")
else:
    print(string, "is not a palindrome.")
