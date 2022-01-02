"""
Number Pattern
Send Feedback
Print the following pattern for n number of rows.
For eg. N = 5

1                1
12            21
123        321
1234    4321
1234554321
Sample Input 1 :
4
Sample Output 1 :
1            1
12        21
123    321
12344321
"""

n=int(input())
totalspace=n*2-2
row=1
while(row<=n):
    column=1
    while column<=row:
        print(column,end='')
        column=column+1
    space=1
    while space<=totalspace:
        print(' ',end="")
        space+=1
    totalspace-=2
    column=row
    while column>0:
        print(column,end='')
        column-=1
    row+=1
    print()