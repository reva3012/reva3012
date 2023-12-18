class laptop():
    chargertype="C-type" #class variable
    def __init__(self):
        self.brand=""   #instance variable
        self.price=34
    def setprice(self,price):  #instance method
        self.price=price
    def getprice(self):
        print(self.price)
    @classmethod
    def changechargertype(cls):     #class method
        cls.chargertype="B TYPE"
        print("charge type changed to B")
    @staticmethod
    def info():         #static method
        print("This is laptop class")


hp=laptop()
hp.setprice(20000)
hp.getprice()

laptop.changechargertype()
hp.info()