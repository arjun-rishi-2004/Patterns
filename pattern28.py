''' 
         *
        * *
       * * *
      * * * *
     * * * * *
      * * * *
       * * *
        * *
         *
n=5
''' 


'''
Approach :
we need to print "* "
Analysing the pattern :
row 1 has 5 cols , with 4 spaces and 1 "* "
row 2 has 5 cols , with 3 spaces and 2 "* "
row 3 has 5 cols , with 2 spaces and 3 "* "
row 4 has 5 cols , with 1 spaces and 4 "* "
row 5 has 5 cols , with 0 spaces and 5 "* "
row 6 has 5 cols , with 1 spaces and 4 "* "
row 7 has 5 cols , with 2 spaces and 3 "* "
row 8 has 5 cols , with 3 spaces and 2 "* "
row 9 has 5 cols , with 4 spaces and 1 "* "

now lets try to derive the solution 

we need two conditions for 
increase and decrease
run outer loop for 2n+1 times 1 to 9
when row<=n:
print whitespace col-row times
print * row times

when row>n:
print whitespace  row - col times

print * 2n-r times
here col====n

'''


n=int(input())

for row in range(1,2*n+1):
    if row<=n:
        whitespace=n-row
        stars=row

    else:
        whitespace=row-n
        stars=2*n-row
    

    print(" "*whitespace,"* "*stars)

n=int(input())
for row in range(1,2*n+1):
    if row<=n:
        for col in range(n-row):
            print(" ",end="")
        for col in range(row):
            print("* ",end="")
    else:
        for col in range(row-n):
            print(" ",end="")
        for col in range(2*n-row):
            print("* ",end="")


    print()
