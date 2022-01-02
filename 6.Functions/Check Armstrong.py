"""
Check Armstrong
Send Feedback
Write a Program to determine if the given number is Armstrong number or not. Print true if number is armstrong, otherwise print false.
An Armstrong number is a number (with digits n) such that the sum of its digits raised to nth power is equal to the number itself.
For example,
371, as 3^3 + 7^3 + 1^3 = 371
1634, as 1^4 + 6^4 + 3^4 + 4^4 = 1634
Input Format :
Integer n
Output Format :
true or false
Sample Input 1 :
1
Sample Output 1 :
true
Sample Input 2 :
103
Sample Output 2 :
false
"""

n=int(input())
no_of_digits=0
org_n=n
orginal_no=n
Armstrong=0
while n>0:
    no_of_digits+=1
    n=n//10
while org_n>0:
    Last_Digit = org_n % 10
    Armstrong  = Armstrong  + ((Last_Digit)**(no_of_digits))
    org_n = (org_n //10)
if orginal_no==Armstrong:
    print("true")
else:
    print("false")