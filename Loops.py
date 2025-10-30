#while loop
"""

i=1
while i<6:
    print("This is while loop")
    i+=1
"""
#if in while loop
"""
i=1
while i<10:
    print("the value of i is:", i)
    i+=1
    if i==6:
        break
        """
#loop with else condition, with the else statement we can run a block of code once when the condition no longer is true:
"""
i=1
while i <6:
    print(i)
    i+=1
else:
    print("i is now  6")
"""
#for loops
#for a in range(1,10):
#    print(a)

#fruits = ["apple", "banana", "cherry"]
#for x in fruits:
 #   print(x)

#for x in "Python":
#    print(x)

# The range() function defaults to 0 as a starting value,
# however it is possible to specify the starting value by adding a parameter: range(2, 6),
# which means values from 2 to 6 (but not including 6):
#The range() function defaults to increment the sequence by 1,
# however it is possible to specify the increment value by adding a third parameter:
# range(2, 30, 3):

#range(start, stop, step)
""""
for x in range(1,10,2):
    print(x)
  """
#Nested Loops
""""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
 """
# for loops cannot be empty but for some reason you have an empty for loop
#put a pass statement in it.
#for x in range(1,10):
 #   pass

#sum of first five natural numbers
sum=0
for i in range(1,6):
    sum+=i
print(sum)



