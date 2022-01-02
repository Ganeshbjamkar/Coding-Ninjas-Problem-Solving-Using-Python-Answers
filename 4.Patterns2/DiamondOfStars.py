"""
Code : Diamond of stars
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
first=n//2+1
sec=n//2
#first loop
for i in range(1,first+1):
    print(" "*(first-i),end="")
    print((2*i-1)*"*",end="")
    print()
#Second Loop
for p in range(1,sec+1):
    print(" "*p,end="")
    print((2*(sec-p+1)-1)*"*",end="")
    print()


# another solution'

n=int(input())
firstHalf=(n+1)//2
secHalf=(n)//2

#First Half
currRow=1
while currRow<=firstHalf:
    spaces=1
    while spaces<=(firstHalf-currRow):
        print(' ',end="")
        spaces+=1
    currcol=1
    while currcol<=(2*currRow)-1:
        print("*",end="")
        currcol+=1
    print()
    currRow+=1

#Secound Half
currRow=secHalf
while currRow>=1:
    spaces=1
    while spaces<=(secHalf-currRow+1):
        print(" ",end="")
        spaces+=1
    currcol=1
    while currcol<=(2*currRow)-1:
        print("*",end="")
        currcol+=1
    print()
    currRow-=1
#Another Solution