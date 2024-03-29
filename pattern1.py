'''
    *****
    *****
    *****
    *****
    *****
'''


'''
Approach:
No of rows(lines)=5
for each line there are 5 stars
row ----- col
1->5
2->5
3->5
4->5
5->5

row is changing from 1 to 5
col is constant

outer loop for row should be from 1 to 5 
inner loop for col should be from 5 

Generalising we have 
outer loop for row should be from 1 to n
inner loop for col should be  n
pattern to print:*
'''

n=int(input())
for row in range(n):
    print("*"*n)

'''Approach 2 
Using nested for loops
Generalising we have 
outer loop for row should be from 1 to n
inner loop for col should be from 1 to n
pattern to print: *

'''

n=int(input())
for row in range(n):
    for col in range(n):
        print("*",end="")
    print()