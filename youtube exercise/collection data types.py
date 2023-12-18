# #1. list[]
# a=[1,2,3,4,5,6]
# a.append(7)     #append using to add any value inside the list data
# print(a)
#
# a=[1,2,3,4,5,6]
# a.insert(6,7)
# a.insert(0,0)#insert using to add value in place of list
# print(a)
#
# a=[1,2,3,4,5]
# a.pop(4)    #pop using to reduce value in list data
# print(a)
#
# a=[1,2,3,4,5,6]
# b=[11,12,13,14,15]
# a.extend(b) #to extend data inside list we use extend
# print(a)
#
# #interview maximum asked quesion is difference b/w list & tuple
#
# #list = we can modify the list .we can remove & add, it allows duplicate
# #2. TUPLE()
# #tuple = we cannot modify tuple. we cannot do changes. it allows duplicate
# a=(1,2,3,4)
# b=list(a)
# b.pop()
# print(a)
# print(b)
#
# #3. SET{}
# # do not allow duplicate values, duplicate values will be removed.we cannot modify the set items but we can add or remove items.
# # sets are unordered.
# # add(),update(),remove(),pop()
# a={1,2,3,4,3,5,1}
# print(a)
# a={1,2,3,4,5}
# a.add(10)
# print(a)
#
# a={1,2,3,4,5}
# a.remove(1)
# print(a)
#
# a={1,2,3,4,5}
# a.pop(4)        #pop always delete 1'st value
# print(a)

#4. dictionary
# do not allow duplicate value,duplicate value will overwrite existing value
# any type of data can be stored
# a={"name":"revathi"}
# print(a)
a = {"name" : "revathi",
     "age" : 30,
     "place" : "usa",
     "travel details" : ["bangalore" , "abudhabi" , "washington" , "baltimore"] }
print(a)

a = {"name" : "revathi",
     "age" : 30,
     "place" : "usa",
     "travel details" : ["bangalore" , "abudhabi" , "washington" , "baltimore"] }
print(a.keys())

a = {"name" : "revathi",
     "age" : 30,
     "place" : "usa",
     "travel details" : ["bangalore" , "abudhabi" , "washington" , "baltimore"] }
a["age"] = 28  # we can update like this
a["color"] = "red"   #we can add like this in distionary
a.update({"age" : 28})
a.pop("travel details")
del a["age"]
print(a.values())  #like this also we can uptade
print(a)