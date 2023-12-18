#boolean values
def program1():
    ram = input("result = ")
    if(ram == "win"):
        print("ram won the prize")
    else:
        print("no prize for ram")

def program2():
    mark = int(input("result = "))
    if(mark > 35):
        print("pass")
    else:
        print("fail")


def program3():
    salary=int(input("income = "))
    age = int(input("age = "))
    if(salary>=25000 or age<=30):
        print("eligible for loan")
    else:
        print("not eligible for loan")



def main():
    program1()
    program2()
    program3()

main()