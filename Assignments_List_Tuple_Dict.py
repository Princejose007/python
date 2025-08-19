#  Find the sum of all elements in a list.

# numbers=[2,4,6,8]
# total=0
# for x in numbers:
#     total=total+x
# print(total)

# Remove duplicates from a list

# numbers=[2,4,2,6,8]
# newlist=[]
# for i in numbers:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)


# Count the frequency of elements in a list. 

# numbers=[2,4,2,6,8,4]
# result={}
# for i in numbers:
#     result[i]=result.get(i,0)+1
# for key, value in result.items():
#     print(f"{key}: {value}")


# Check if a list is a palindrome
 
# def is_pallindrome(list):
#     return list==list[::-1]
# list1=[1,2,2,,1]
# if is_pallindrome(list1):
#     print("it is Pallindrome")
# else:
#     print("It is not a pallinndrome")



# list1=[2,4,1,7,2]
# list2=[6,3,2,5]
# list1.extend(list2)
# print(list1)
# list1.sort()
# print("sorted:",list1)


# Find the common elements in two lists. 

# list1=[2,4,1,7,2]
# list2=[6,3,2,5,8,9,4]
# common=[]
# for item in list1:
#     if item in list2 and item not in common:
#         common.append(item)

# print(common)


# Create a tuple and print each element using a loop. 

# fruits=("apple","orage","mango")
# for i in fruits:
#     print(i)

# Convert a list to a tuple. 

# list1=[2,4,1,7,2]
# for i in list1:
#     tup=tuple(list1)
# print(tup)

# Find the index of an element in a tuple. 


# number=(2, 4, 1, 7, 2)
# num=int(input("enter the element: "))

# for i in range(len(number)):
#     if number[i]==num:
#         print(i)


# Check if an element exists in a tuple. 


# number=(2, 4, 1, 7, 2)
# num=int(input("Enter the element: "))
# if num in number:
#       print("Elemnts found")
# else:
#      print("element not found")


# Count the number of occurrences of an item in a tuple.

# number=(2, 4, 1, 7, 2)
# num=2
# flag=0
# for i in range(len(number)):
#     if number[i]==num:
#         flag+=1
# print(flag)

#Find the length of a tuple. 
# number=(2, 4, 1, 7, 2,5,2,7)
# flag=0
# for i in (number):
#     flag+=1
# print(flag)

#  Concatenate two tuples.

# y=(2,4,3,5,6)
# x=(4,5,6,7)
# y1=list(y)
# x1=list(x)

# con=x1+y1
# final=tuple(con)
# print(final)


#Convert a tuple to a list and modify it. 

# number=(2, 4, 1, 7, 2)
# num=list(number)
# print(num)
# del num[2]
# print(num)
# number=tuple(num)
# print(number)


#Create a dictionary and print all key-value pairs.

# dict1={
#     "name":"prince",
#     "age":21,
#     "place":"thrissur"
# }

# print(dict1)



#Add, update, and delete a key-value pair in a dictionary. 

# dict1={
#     "name":"prince",
#     "age":21,
#     "place":"thrissur"
# }


# dict1.update({"phone:no":7554687764})
# print(dict1)


#  Find the key with the maximum value in a dictionary. 


# scores = {
#     'Alice': 85,
#     'Bob': 92,
#     'Charlie': 78
# }

# top=0
# name=""
# for x,y in scores.items():
#     if y>top:
#         top=y
#         name=x
# print(top)
# print(name)




# dict1={
#     "name":"prince",
#     "age":21,
#     "place":"thrissur"
# }

# scores = {
#     'Alice': 85,
#     'Bob': 92,
#     'Charlie': 78
# }

# method 1
# dict1.update(scores)
# print(dict1)

# method2

# merge=dict1|scores
# print(merge)



#  Count the frequency of characters in a string using a dictionary. 

# text="princejose"
# frequency={}
# for i in text:
#     if i in frequency:
#         frequency[i]+=1
#     else:
#         frequency[i]=1
# print(frequency)



#  Check if a key exists in a dictionary. 


# dict1={
#     "name":"prince",
#     "age":21,
#     "place":"thrissur"
# }

# check="age"

# for i in dict1.keys():
#     if i==check:
#         print("it exist")
#         found=True
#         break
# if not found:
#     print("not exist")


#  Create a dictionary from two lists (keys and values). 


# name=["prince","noyal","das"]
# score=[97,65,78]

# result=dict(zip(name,score))
# print(result)