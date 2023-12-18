# def painter():
#     print("painting")
# painter()
#
# def painter(msg):
#     print("message : " , msg)
# painter("paint my house")
#
# def findevenorodd(b):
#     if(b%2==0):
#         print("even")
#     else:
#         print("odd")
#
# a=int(input("Enter a = "))
# findevenorodd(a)
#
# def findpassorfail(result):
#     if(result>=35):
#         print("pass")
#     else:
#         print("fail")
# mark=int(input("enter the mark = "))
#
# findpassorfail(mark)

def printrange(r1 , r2):
    for i in range (r1 , r2):
        print(i)
a=int(input("enter a:"))
b=int(input("enter b:"))
printrange(a,b)