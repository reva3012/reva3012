class goa:
    name = ""
    drink = ""
    def party(self):
        print("Lets party.....")
    def beach(self):
        print("Enjoying the beach")

ramesh = goa()
suresh = goa()

ramesh.name = "Ramesh"
suresh.name = "Suresh"

ramesh.drink ="yes"
suresh.drink ="no"

print(ramesh.name)
print("drink:",ramesh.drink)
ramesh.party()
print(suresh.name)
print("drink:" ,suresh.drink)
suresh.beach()


class laptop:
    price=""
    processor=""
    ram=""
    def hp(self):
        print("HP")
    def dell(self):
        print("DELL")
    def lenovo(self):
        print("LENOVO")

hp=laptop()
dell=laptop()
lenovo=laptop()

hp.price=50000
hp.processor="i5"
hp.ram="8GB"

dell.price=70000
dell.processor="i7"
dell.ram="16GB"

lenovo.price=80000
lenovo.processor="i7"
lenovo.ram="128GB"

print(hp.price)
print(dell.processor)
print(lenovo.ram)
