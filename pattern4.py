'''
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5

'''

'''
Approach:
no of rows :5
no of cols per row differs
row----col
1----1
2----2
3----3
4----4
5----5

Fine , similar to pattern 2 

No of cols of the row is equal to value of the iterator i 
pattern to be printed varies ie integers 

outer loop runs for n times from 1 to n+1
row =1 2 3 4 5 
col for row 1 is 1 (1)
col for row 2 is 1 2 (2)
col for row 3 is 1 2 3 (3)
row no === no of col in row
that is col varies from 1 to row+1

lets print the value of col
we are printing the col number 



'''

n=int(input())
for row in range(1,n+1):
    for col in range(1,row+1):
        print(col,end=' ')
    print()