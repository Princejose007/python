#Anonymus or lamda functions
# x=lambda a : a+10
# print(x(5))

# x=lambda a , b , c : a + b + c
# print(x(5,6,7))


#types of anonymmus function
#1 with map()
# num=[1,2,3,4]
# square=list(map(lambda x:x**2,num))
# print(square)

#2nd with filter()
# nums=[1,2,3,4,5]
# even=list(filter(lambda x: x%2==0,nums))
# print(even)

#3rd with reduce()
# from functools import reduce
# nums=[1,2,3,4]
# product=reduce(lambda x,y: x*y,nums)
# print(product)

