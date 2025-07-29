 #1.Print numbers from 1 to 10 using a for loop.


# for i in range (1,11):
#     print(i)

#2. Print even numbers between 1 and 20 using a while loop.

# i=0
# while i<20:
#     i+=1
#     if(i%2==0):
#         print(i)


 #3. Print the multiplication table of a number using for loop.


# x=int(input("Enter the number:"))
# for i in range(1,11):
#     print(i*x)
#     i+=1  


# 4. Check if a number is prime using for loop.


# n=int(input("Enter a number: "))
# i=1
# flag=0
# for i in range(i,n+1):
#     if n%i==0:
#         flag+=1
# if flag==2:
#     print("it is prime number ")
# else:
#     print("it is not a prime number")


# 5.  Find factorial of a number using for loop.


# n=int(input("Enter the number:"))
# i=1
# fact=1
# for i in range(i,n+1):
#     fact=fact*i
#     i+=1
# print(fact)


#  6. Write a program to print numbers from 1 to 10. Use break to stop when the number is 5.

# i=1
# while i<11:
#     print(i)
#     if i==5:
#         break
#     i+=1
    


# 7. Print numbers from 1 to 10, skipping the number 7 using continue.

# i=1
# while i<10:
#     i+=1
#     if i==7:
#         continue
#     print(i)

# 8. Print all numbers from 1 to 20, but skip numbers divisible by 3 using continue.

# i=0
# while i<20:
#     i+=1
#     if i%3==0:
#         continue
#     print(i)
    
# 9. Print numbers from 1 to 100. Use break when the first number divisible by both 4 and 6 is found.


# i=0
# while i<100:
#     i+=1
#     if (i%4==0 and i%6==0):
#         break
#     print(i)

#10. Print 1 to 100, Skip 10 to 20: Use continue to skip numbers from 10 to 20 in a for loop from 1 to 100.



# for i in range(0,100):
#     if (i>=10 and i<=20):
#         continue
#     print(i)

