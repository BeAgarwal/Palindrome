''' Code by Shubham Agarwal
    Link: https://github.com/BeAgarwal/Palindrome '''

'''Program to find all palindrome numbers of given digit.'''

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

for i in range(rangefrom, rangeto):
    ans = check_palindrome(i)
    if ans:
        print(i, end = ",")
      

'''OUTPUT
Enter the digit: 4
1001,1111,1221,1331,1441,1551,1661,1771,1881,1991,2002,2112,2222,2332,2442,2552,2662,2772,2882,2992,3003,3113,3223,3333,
3443,3553,3663,3773,3883,3993,4004,4114,4224,4334,4444,4554,4664,4774,4884,4994,5005,5115,5225,5335,5445,5555,5665,5775,
5885,5995,6006,6116,6226,6336,6446,6556,6666,6776,6886,6996,7007,7117,7227,7337,7447,7557,7667,7777,7887,7997,8008,8118,
8228,8338,8448,8558,8668,8778,8888,8998,9009,9119,9229,9339,9449,9559,9669,9779,9889
'''
