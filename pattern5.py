'''
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
for n=5
'''

'''
Approach:
no of rows here is not given directly 

for n=5 , we have to print 9 rows 
that is , normal pyramid 1 to 5 and reverse pyramid 5 to 1 
where 5 is common so we have 9 rows 

for n=5 , we have 2n-1 rows

outer loop will run for 2n-1 times
lets understand the pattern 

the number of cols in each row increase until a point that point is where row iterator is equal after that number of cols in each row decrease

that is 
for n=5
row --- col 
1---1
2---2
3---3
4---4
5---5  (row==n)
6---4
7---3
8---2
9---1

lets try to derive a formula
outer loop runs from 1 to 2n(i:1 to 9)
two parts
when row<=n:
run inner loop for row times 

when row>n
run inner loop for 2n-row times 


'''
n=int(input())
for row in range(1,2*n+1):
    if row <=n :
        for col in range(row):
            print("*",end='')
    if row>n:
        for col in range(2*n-row):
            print("*",end='')
    print()


n=int(input())
stars=1
for row in range(1,2*n):
    if row<=n:
        stars=row
    else :
        stars=2*n-row
    print(stars*"*",end='\n')

