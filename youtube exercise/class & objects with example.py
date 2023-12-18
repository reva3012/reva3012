# question 1:  create a class called student
# create a variable = name and register number using constrctor.
# create a function called display which should display the name and register number of the student
def pro1():
    class student:
        def __init__(self): #constructor
            self.name="rejbjgyfti"
            self.registerno="65465"
        def display(self):
            print("name",self.name)
            print("register No",self.registerno)

    s1=student()
    s2=student()

    s1.name="revathi"
    s1.registerno="1"

    s2.name="manju"
    s2.registerno="2"
    s1.display()
    s2.display()

# question 2:  create a class called fruit
# create a variable called color using __init__ method.
# create object called apple "pass the color variable as a parameter through object"
#
def pro2():
    class fruit:
        def __init__(self):
            self.color="black"

    apple=fruit()
    apple.color="red"
    print(apple.color)
    #AS A QUESTION ANSWER
    class fruit:
        def __init__(self,colo):
            self.color=colo

    apple=fruit("red")
    print(apple.color)

# question 3:  create a class called teacher
# create a variable = name and register number using constrctor.
# create a function called display which should display the name and register number of the teacher
# create t1 and t2 object and pass the name and reg no value through object

def pro3():
    class teacher:
        def __init__(self,name,reg):
            self.name=name
            self.regno=reg
        def display(self):
            print("name",self.name)
            print("regno",self.regno)
    t1=teacher("ramya","1")
    t2=teacher("ram","2")
    t1.display()
    t2.display()

#  create a class called calculator
#  create 2 variables a & b
# create a function called add,sub,mul,div all functions should take 2 variables as parameter
# pass the a and b value through objects()
def pro4():
    class calculator:
        def __init__(self,a,b):
            self.num1=a
            self.num2=b
        def add(self):
            print("add", self.num1+self.num2)
    obj1=calculator(13,2)
    obj1.add()
# another way
class calculator:
    def add(self,a,b):
        print("add" ,a+b)
        print("sub" , a-b)
        print("mul" , a*b)
        print("div" , a/b)
obj1=calculator()
obj1.add(10,5)





def main():
    pro1()
    pro2()
    pro3()
    pro4()

main()