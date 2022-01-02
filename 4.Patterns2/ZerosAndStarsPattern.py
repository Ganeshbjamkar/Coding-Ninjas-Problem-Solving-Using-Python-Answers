"""
Zeros and Stars Pattern
Send Feedback
Print the following pattern
Pattern for N = 4
*000*000*
0*00*00*0
00*0*0*00
000***000
Input Format :
N (Total no. of rows)
Output Format :
Pattern in N lines
Sample Input 1 :
3
Sample Output 1 :
*00*00*
0*0*0*0
00***00
Sample Input 2 :
5
Sample Output 2 :
*0000*0000*
0*000*000*0
00*00*00*00
000*0*0*000
0000***0000
"""

n=int(input())
start=1
end=2*n+1
mid=n+1
row=1
while(row<=n):
    column=1
    while column<=(2*n+1):
        if column==start or column==end or column==mid:
            print("*",end='')
        else:
            print("0",end="")
        column=column+1
    start=start+1
    end=end-1
    row=row+1
    print()