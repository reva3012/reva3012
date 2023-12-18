#the for loop is usually used when the number of iterations is known
#the while loop is usually used when the number of iterations is unknown
# i=0
# while(i==0):
#     print(i)
#     i=1;
#
#print a number from 1 to 5 using while loop
# i=1
# while(i<6):
#     print(i)
#     i=i+1

i=10
while(i<=200):
    print(i,end=" , ")#if numbers need n single line have to add end=" , "
    i=i+10
#print a program print 1st 10 natural numbers in reverse order

i=10
while(i>0):
    print(i,end=" ")
    i=i-1
# write a prgm to find the factorial of the number(5=5*4*3*2*1)
i=3
fact=1
while(i>0):
    fact=fact*i
    i=i-1
print(fact)

