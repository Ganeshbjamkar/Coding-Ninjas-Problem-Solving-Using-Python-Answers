"""
Sum of n numbers
Send Feedback
Given an integer n, find and print the sum of numbers from 1 to n.
Note : Use while loop only.
Input Format :
Integer n
Output Format :
Sum
Constraints :
1 <= n <= 100
Sample Input :
10
"""

n = int(input())
sum = 0
# loop from 1 to n
for num in range(1, n + 1, 1):
    sum = sum + num
print(sum)
