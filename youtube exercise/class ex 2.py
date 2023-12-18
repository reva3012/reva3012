class laptop:
    def __init__(self):  #the main purpose of a constructor is to initialize or assign values to the data members of that class
         self.price=0
         self.ram=""
         self.processor=""
    def display(self):
        print("display")
hp=laptop()
hp.price=50000
hp.ram="8gb"
hp.processor="i5"
print(hp.ram )

