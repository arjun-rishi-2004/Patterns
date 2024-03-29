'''
    *****
    ****
    ***
    **
    *
'''

'''
Approach:
No of rows:5 
no of cols per row differs
row ----- col
1----5
2----4
3----3
4----2
5----1

As row iterator increase column iterator decreases 

When row is 1 , col is 5
for row 1 print * n times
for row 2 print * n-1 times


'''

n=int(input())

row=0
while(row<n):
    col=n
    while(col>0):
        print("*",end='')
        col-=1

    print()
    n-=1




n = int(input())
row = 0
while row < n:
    col = n
    while col > row:
        print("*", end='')
        col -= 1
    print()
    row += 1


n = int(input())

for row in range(n,0,-1):
    for col in range(row):
        print("*",end='')
    print()



#derived from pattern 2 as a formula
n=int(input())
for row in range(1,n+1):
    for col in range(n-row+1):
        print("*",end='')
    print()
