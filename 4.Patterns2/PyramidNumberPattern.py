"""
Pyramid Number Pattern
Send Feedback
Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234
Input format : N (Total no. of rows)

Output format : Pattern in N lines

Sample Input :
5
Sample Output :
        1
      212
    32123
  4321234
543212345
"""

n = int(input())
num = 1
gap = n - 1
for j in range(1, n + 1):
    num = j
    for i in range(1, gap + 1):
        print(" ", end="")
    gap = gap - 1

    for i in range(1, j + 1):
        print(num, end="")
        num-=1
    num=2
    for i in range(1, j):
        print(num, end="")
        num+=1

    print()