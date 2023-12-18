for i in "apple":
    print(i)
for i in range(5):
    print(i)
for i in range(1,5):
        print(i)

print 2 table using for loop
for i in range(1,11):
    print(i ,"*2 = ", i*5)

# get input for number a& b
print number b/w a & b
sample input 8 & 15
sample output 9,10,11,12,13,14
a=int(input("a="))
b=int(input("b="))
for i in range(a+1,b):
    print(i)

# print even number b/w 1 to 10
a=2
if a%2==0:
    print("even")
for i in range(1,11):
    if(i%2==0):
        print(i)

# count the no of odd no's b/w 1 to 10
count=0
for i in range(1,11):
    if(i%2==0):
        count=count+1
print(count)
# count odd &even nos 1 to 5
e_count=0
o_count=0
for i in range (1,11):
    if(i%2==0):
        e_count=e_count+1
    else:
        o_count=o_count+1
print(e_count)
print(o_count)
# count the number which are divisible by 3 & 5
count=0
for i in range(1,101):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)