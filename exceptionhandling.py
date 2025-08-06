#Exception handling
#try & axcept and else,finally


#try &except

#try:
#--->    #code that may cause exceptions

#except
#--->    #code to run when exception ocuurs



# try:
#     numerator=10
#     denominator=0
#     result=numerator/denominator
#     print(result)
# except:
#     print("Error: Denominator cannot be divisible by 0")


# try:
#     even_numbers=[2,4,6,8]
#     print(even_numbers[5])
# except IndexError:
#     print("Index out of bound")


#program to print the reciprocal of  even numbers


# try:
#     num=int(input("Enter a number : "))
#     assert num%2==0
# except:
#     print("Not a even number!")
# else:
#     reciprocal=1/num
#     print(reciprocal)


#finally ---> allowed exception

# try:
#     numerator=10
#     denominator=0

#     result=numerator/denominator
#     print(result)
# except:
#     print("Error :dominator cannot be 0")

# finally:
#     print("This is finally block ")  #--->finally will always work



# try:
#     f=open("example.txt","r")
#     contend=f.read()
# except FileNotFoundError:
#     print("file not found")

# finally:
#     print("closing file(if oriented)")
#     try:
#         f.close()
#     except:
#         pass









