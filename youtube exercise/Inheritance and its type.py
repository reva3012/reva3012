# class dad():
#     def phone(self):
#         print("dad's phone")
# class mom():
#     def sweet(self):
#         print("mom's sweet")
# class son(dad,mom):
#     def laptop(self):               #multiple inheritance
#         print("son's laptop")
#
# ram=son()
# ram.phone()
# ram.sweet()

#
# class grandpa():
#     def phone(self):
#         print("grandpa phone")
# class dad(grandpa):
#     def money(self):
#         print("dads money")
# class son(dad):         #multi level inheritance
#     def laptop(self):
#         print("sons laptop")
# ram = son()
# ram.laptop()
# ram.money()
#
# d1= dad()
# d1.phone()
#
# class dad():
#     def money(self):
#         print("dads money")
#
# class son1(dad):
#     pass
# class son2(dad):            #hierarchical inheritance
#     pass
# class son3(dad):
#     pass
#
# s2 = son2()
# s2.money()


class dad():
    def money(self):
        print("dads money")
class land():
    def Important(self):
        print("Important land")

class son1(dad,land):
    pass
class son2(dad):            #multiple inheritance
    pass
class son3(dad):
    pass

s2 = son2()
s2.money()

# single
# multiple
# multilevel
# hierartical=hybrid inheritance