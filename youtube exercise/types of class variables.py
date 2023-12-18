# class phone:
#     def __init__(self,brand,price,chargertype):
#         self.brand=brand
#         self.price=price
#         self.chargertype=chargertype
#     def display(self):
#         print("Brand : ",self.brand)
#         print("Price : ",self.price)
#         print("Chargertype : ",self.chargertype)
# samsung = phone("samsung","25000","C-type")
# samsung.display()
# redmi = phone("redmi","15000","C-type")
# redmi.display()
# moto = phone("redmi","15000","C-type")
# moto.display()
# for all mobile charger type is C type (here we have to use class variable
class phone:
    chargertype="C-type"
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price
    def display(self):
        print("Brand : ",self.brand)
        print("Price : ",self.price)
        print("Chargertype : ",self.chargertype)
samsung = phone("samsung","25000")
samsung.display()
redmi = phone("redmi","15000")
redmi.display()
moto = phone("moto","15000")
moto.display()