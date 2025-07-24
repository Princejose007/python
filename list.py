# fruits=["apple","orange","pineapple"]
# print(fruits)


# print(fruits[1])


# fruits=["apple","orange","pineapple"]
# fruits[0]="bannana"
# print(fruits)

# varable chaging using range specified
# fruits=["apple","orange","pineapple","cherry","bannana","mango"]


# fruits[1:3]=["blackberry","watermelon"]
# print(fruits)



#insert item

# fruits=["apple","orange","pineapple"]
# fruits.insert(2,"cherry")
# print(fruits)

#Appending / to add in the last position

# fruits=["apple","bannana","cherry"]
# fruits.append("orange")
# print(fruits)

#Extend list(mergin two list)
# fruits=["apple","bannana","cherry"]
# vegetable=["spinach","bettroot","carrot"]
# fruits.extend(vegetable)
# print(fruits)

#remove /for removing from list
# fruits=["apple","bannana","cherry"]
# fruits.remove("bannana")
# print(fruits)  #if there is multiple bannana the first one will removed


#To remove specific variable

# fruits=["apple","bannana","cherry"]
# fruits.pop(1)
# print(fruits) # to remove a specific from list



# using #del() for removing
# fruits=["pinapple","cherry","apple"]
# del fruits[0]
# print(fruits)

# fruits=["pinapple","cherry","apple"]
# fruits.clear()
# print(fruits)

#clear the list /removing the elemths only not also the variable
# fruits=["pinapple","cherry","apple"]

# fruits.clear()
# print(fruits)


#loop in index
# fruits=["apple","orange","grape"]
# for i in range(len(fruits)):
#     print(fruits[i])

#list comprehension


# fruits=["apple","bannana","cherry","orange","blackberry"]
# newlist=[]
# for x in fruits:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)


#list comprehension another method 
# fruits=["apple","bannana","cherry","orange","blackberry"]
# newlist=[x for x in fruits if "a" in x]
# print(newlist)


#sort accending 
# fruits=["apple","bannana","cherry","orange","blackberry"]
# fruits.sort()
# print(fruits)


#sort decending
# fruits=["apple","bannana","cherry","orange","blackberry"]
# fruits.sort(reverse=True)
# print(fruits)


# numbers=[100,77,99,44,66]
# numbers.sort(reverse=True)
# print(numbers)



#copy

# fruits=["apple","bannana","cherry","orange","blackberry"]
# diet=fruits.copy()
# print(diet)


#using list function to copy
# fruits=["apple","bannana","cherry","orange","blackberry"]
# diet=list(fruits)
# print(diet)


#adding list using + operator as usual list1+list2


#appending methode
# list1=[1,4,2,5]
# list2=[8,3,5,1]
# for x in list2:
#     list1.append(x)
# print(list1)


#extending method
# list1=[1,4,2,5]
# list2=[8,3,5,1]
# list1.extend(list2)
# print(list1)