"""
Code : Mirror Number Pattern
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4

. . .1 . . 1 2 . 1 2 3 1 2 3 4 

The dots represent spaces.



Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Constraints
0 <= N <= 50
Sample Input 1:
3
Sample Output 1:
      1 
    12
  123
Sample Input 2:
4
Sample Output 2:
      1 
    12
  123
1234
"""

n=int(input())
currRow=1
while currRow<=n:
    currCol=1
    spaces=1
    while spaces<=n-currRow:
        print(" ",end="")
        spaces+=1
    while currCol<=currRow:
        print(currCol,end="")
        currCol+=1
    print()
    currRow+=1