"""
Code : Star Pattern
Send Feedback
Print the following pattern
Pattern for N = 4



The dots represent spaces.



Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Constraints :
0 <= N <= 50
Sample Input 1 :
3
Sample Output 1 :
   *
  *** 
 *****
Sample Input 2 :
4
Sample Output 2 :
    *
   *** 
  *****
 *******
"""
n=int(input())
currRow=1
while currRow<=n:
    spaces=1
    while spaces<=n-currRow:
        print(" ",end="")
        spaces+=1
    currCol=1
    while currCol<=(2*currRow)-1:
        print("*",end="")
        currCol+=1
    print()
    currRow+=1