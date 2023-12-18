def pro1():
    score = int(input("score percentage = "))
    if(score>=70):
        name = input("enter your name = ")
        age = input("enter your age = ")
        print("you are eligible ")
    else:
        print("you are not eligible")


# if we are using AND we have to consider multipication(0*1)
# if we are using OR we have to consider addition(0+1)

def pro2():
    salary = float(input("income = "))
    age = int(input("age = "))
    if(salary>=20000 or age <=25):
        loan = int(input("loan = "))
        if(loan>55000):
            print("maximum loan amount is 550000")
        else:
            print("eligible for loan")
    else:
        print("not eligible for loan")
# ifelse program inside one more ifelse works its called nestedif program

def pro3():

    T = int(input("tamil = "))
    E = int(input("english = "))
    M = int(input("maths = "))
    S = int(input("science = "))
    S_S = int(input("S-Science = "))
    Total = (T+E+M+S+S_S)/5
    if(Total<35):
        print("additional class required")
    else:
        print("you are good to go")

def main():
    pro1()
    pro2()
    pro3()

main()