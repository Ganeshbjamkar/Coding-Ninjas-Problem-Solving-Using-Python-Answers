"""
Palindrome number
Send Feedback
Write a program to determine if given number is palindrome or not. Print true if it is palindrome, false otherwise.
Palindrome are the numbers for which reverse is exactly same as the original one. For eg. 121
Sample Input 1 :
121
Sample Output 1 :
true
Sample Input 2 :
1032
Sample Output 2 :
false
"""
# 1)
def checkPalindrome(n):
    Revese = 0
    while n > 0:
        Remainder = n % 10
        n = int(n / 10)
        Revese = Revese * 10 + Remainder
    return Revese


num = int(input())
Rev=checkPalindrome(num)
if (num==Rev):
    print('true')
else:
    print('false')

# 2) solution

num = int(input())
real_num=num
test_num = 0
while (num > 0):
    remainder = num % 10
    test_num = (test_num * 10) + remainder
    num = num // 10
if int(test_num)==real_num:
    print("true")
else:
    print("false")