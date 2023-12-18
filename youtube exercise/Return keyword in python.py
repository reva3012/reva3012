# def teacher():
#     return "I am a teacher"
# msg = teacher()
# print(msg)
#
# def valueofa():
#     return 10
# a = valueofa()
# print(a)

s_username="emc"
s_password='123'
username=input("Enter value for username : ")
password=input("Enter value for password : ")
def validate():
    if(s_username==username and s_password==password):
        return True
    else:
        return False
a=validate()
print(a)

def add(n1 , n2):
    return n1+n2

a=int(input("Enter a value = "))
b=int(input("Enter b value = "))
c=int(input("Enter c value = "))
added=add(a,b)
output=added*c
print(output)
