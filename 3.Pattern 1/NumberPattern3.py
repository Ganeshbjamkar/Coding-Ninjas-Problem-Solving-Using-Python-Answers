"""
Number Pattern 3
Send Feedback
Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
121
1221
Input format :
Integer N (Total no. of rows)
Output format :
Pattern in N lines
Sample Input :
5
Sample Output :
1
11
121
1221
12221
"""

n=int(input())
i=1
print(1)
while i<=n-1:
    print("1",end="")
    num_2=2
    while num_2<=i: #no of Colums
        print("2",end="")
        num_2+=1
    print("1")
    i=i+1