"""
Diamond of Stars
Send Feedback
Print the following pattern for the given number of rows.
Note: N is always odd.


Pattern for N = 5



The dots represent spaces.



Input format :
N (Total no. of rows and can only be odd)
Output format :
Pattern in N lines
Constraints :
1 <= N <= 49
Sample Input 1:
5
Sample Output 1:
  *
 ***
*****
 ***
  *
Sample Input 2:
3
Sample Output 2:
  *
 ***
  *
"""


n=int(input())
n1=(n//2)+1
for i in range(1,n1+1):
    for j in range(1,n1-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()
n2=n-n1
for i in range(n2,0,-1):
    for j in range(1,n1-i+1):
        print(" ",end="")
    for j in range(1,2*i):
        print("*",end="")
    print()