def pro1():
    a = int(input("a"))
    b = int(input("b"))
    c = int(input("c"))
    d = a * b * c
    e = a + b + c
    f = d / e
    print(f)

def pro2():
    name = input()
    score = int(input())
    department = input()
    print("student name is : ", name)
    print("student score is : ", score / 10, "/10")
    print("student department is : ", department)

def main():
    pro1()
    pro2()

main()