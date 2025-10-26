import keyword
#this will print all the reserved keywords of python
# print(keyword.kwlist)
# print(type(keyword.kwlist)) # this will print the type of kwlist that is list
# print(len(keyword.kwlist)) #length of keyword, len() is a predefined function which gives the length but it needs an object(string, list, any object) tobe passed.
# s1 = "Python is fun"
# print(len(s1))

#conditional statements
# animal = input("Enter animal type \n")
# if(animal=="dog"):
#     print("This is Dog")
#
# age=18
# if(age>=18):
#     print("citizen is eligible to work")

# #shorthand if
#age = int(input("enter your age:"))
#if age>=18: print("you are eligible to work")

#if -else
#age = int(input("enter your age:"))
#if age >= 18:
 #   print("you are old enough to vote")
#else:
 #   print("you are not eligible to vote")

#Nested If Else
marks= 85
if marks>=33 and marks<=35:
    print("Grade:D")
elif marks>= 36 and marks<=50:
    print("Grade:C")
elif marks>=55 and marks<=70:
    print("Grade:B")
else:
    print("Grade:A")


