def pro1():

    score=int(input("Enter the score = "))
    if(score<35):
        print("poor student")
    if(score>35 and score<70):
        print("average student")
    if(score>70):
        print("good student")
    # we use if for every line it will take too much time to run a program(real time program have so many lines)
    #instead program(elif)
def pro2():
    score =int(input("Enter the score = "))
    if(score<35):
        print("poor student")
    elif(score<35 and score>70):
        print("average student")
    else:
        print("good student")
    #it gets output in 1st line next lines wont work
def pro3():
    score =int(input("Enter the score = "))
    if(score<=35):
        print("poor student")
    elif(score>35 and score<=70):
        print("average student")
    elif(score>70 and score<=100):
        print("good student")
    else:
        print("invalid score")
def pro4():
    a = int(input("A = "))
    b = int(input("B = "))
    operation = input("add/sub/mul/div : ")
    if (operation == "add"):
        print(a + b)
    elif (operation == "sub"):
        print(a - b)
    elif (operation == "mul"):
        print(a * b)
    elif (operation == "div"):
        print(a / b)
    else:
        print("invalid operation")

def main():
    # pro1()
    # pro2()
    # pro3()
    pro4()
main()