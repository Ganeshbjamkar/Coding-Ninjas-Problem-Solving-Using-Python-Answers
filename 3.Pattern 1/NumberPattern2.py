"""
Number Pattern 2
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
202
3003
Input format :
Integer N (Total no. of rows)
Contraints:
1 <= n <= 50
Output format :
Pattern in N lines
Sample Input :
5
Sample Output :
1
11
202
3003
40004
"""

n=int(input())
i=1
print(1)
while i<=n-1:
    print(i,end="")
    num_2=2
    while num_2<=i: #no of Colums
        print("0",end="")
        num_2+=1
    print(i)
    i=i+1