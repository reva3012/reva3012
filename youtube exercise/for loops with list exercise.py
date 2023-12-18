# write a program to display n terms of natural no's and their sum test data:7'
import math
def pro1():

    a=[]
    print("Enter natural numbers: ")
    for i in range(7):
        num=int(input("enter numbers:"+str(i+1)))
        a.append(num)
    print(a)

    sum = 0
    for i in a:
        sum=sum+i
    print(sum)

def cube(num):
    #
    #
    #
    #
    #print("I am inside CUBE")
    return num * num * num
def pro2():

    # write a program to display the cube of the number up to an integer
    # input number of terms : 5

    sum = 0
    for i in range(1, 6):
        # print(f"Number is : {i} and cube of the {i} is :", (i * i * i))
        print(f"Number is : {i} and cube of the {i} is :", (cube(i)))

def main():
    #pro1()
    pro2()
main()
