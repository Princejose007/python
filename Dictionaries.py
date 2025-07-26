# dict1={
#     "brand" : "ford",
#     "model" : "mustang",
#     "year" : 1964
# }
# print(dict1)

# print(dict1["brand"])
# print(len(dict1))# to find length

#Accessing using get method
# x=dict1.get("model")
# print(x)

#adding new key value pair

# car={
#     "brand":"ford",
#     "model":"mustang",
#     "year":1964
# }

# x=car.keys()
# print(x)

#to get both key and value
# x=car.items()
# print(x)


#updating dicitinory
# car["year"]=2018
# print(car)

# car={
#     "brand":"ford",
#     "model":"mustang",
# }
# #To add a new key and pair
# car.update({"year":2020})
# print(car)


#Remove item


car={
    "brand":"ford",
    "model":"mustang",
    "year":1964
}

# car.pop("year")
# print(car)


#to  remove the last item

# car.popitem()
# print(car)

#Delection
#del function is used to remove a complete key value pair from dictionary


# del car["model"]
# print(car)

#clear() it is used to clear the entire key value pairs in dictinory

# car.clear()
# print(car)


#loop
# for x in car.keys():
#     print(x)


# for x,y in car.items():
#     print(x,y)


#copy
#1
# print(mydict)
# mydict=car.copy()


#2
# mydict=dict(car)
# print(mydict)

#nested dictionarys


# myfamily={
#     "child1":{
#         "name":"emanuvel",
#         "year":"2004"
#     },
#     "child2":{
#         "name":"Tobias",
#         "year":2007
#     },
#     "child3":{
#     "name":"linus",
#     "year":2011
#     }
# }
# print(myfamily)