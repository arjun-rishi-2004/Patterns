'''
    *
    **
    ***
    ****
    *****
    
'''

'''
Approach:

No of lines rows=5
No of cols for each row differs 

row ---- col
1---1
2---2
3---3
4---4
5---5

ie the i th row has i cols
Generalising the concept:
no of lines rows=n
no of cols = no of that row 
pattern of be printed =*

'''

n=int(input())
for row in range(1,n+1):
    for col in range(row):
        print("*",end='')
    print()
