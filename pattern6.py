'''
         *
        **
       ***
      ****
     *****

'''

'''
Approach:

no of rows = 5
no of columns per row

row---col
1---1
2---2
3---3
4---4
5---5

but the col is printed in the reverse order 

the outer loop has to run n times from 1 to n+1

the inner loop has to run n times but it should print * in reverse 
how ?????
 

lets analyse the pattern

        col 1 2 3 4 5
    row
     1              *
     2            * *
     3          * * *
     4        * * * *
     5      * * * * *

for row 1 it prints *  1time 
for row 2 it prints * 2 times
...
no of times is not an issue ,
to not print first 4 cols on row 1 what should we do ?
print something else like whitespace or just skip those cols

fine how to do it?
when to print * when to print whitespace

for every row r , we need n-r whitespaces ,after that condition print * 

so this is it :
print n rows 
print n cols
but for every row , print n-r whitespace and remaining stars


lets try it out
'''
n=int(input())
for row in range(1,n+1):
    for col in range(1,n+1):
        if col<n+1-row:
            print(" ",end='')
        else:
            print("*",end='')

    print()
