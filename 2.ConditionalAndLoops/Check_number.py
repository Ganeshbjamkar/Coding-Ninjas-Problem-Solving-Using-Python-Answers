"""
Check number
Send Feedback
Given an integer n, find if n is positive, negative or 0.
If n is positive, print "Positive"
If n is negative, print "Negative"
And if n is equal to 0, print "Zero".
Input Format :
Integer n
Output Format :
"Positive" or "Negative" or "Zero" (without double quotes)
Constraints :
-100 <= n <= 100
"""

n = int(input())

if n >= 1:
    print("Positive")
elif n <= -1:
    print("Negative")
elif n == 0:
    print("Zero")