import copy
#Arrays are used to store multiple values in one single variable

cars = ["ford","ferari","bmw", "honda"]
"""
cars = ["ford","ferari","bmw", "honda"]
for i in cars:
    print(i)
"""
#len() method returns the length of an array.
"""
x=len(cars)
print(x)
"""
#Array methods

#append(): Adds an element at the end of the list
"""cars.append("Mahindra")
print(cars)

#copy(): Returns a copy of the list
vehicle= copy.copy(cars)
print(cars)

#extend():Add the elements of a list (or any iterable), to the end of the current list
cars.extend("Toyota")
print(cars)
"""

S= "Isha"
index_of_h= S.index("h")
print(index_of_h)
#index_of_i= S.index("i") #this will give error as small i is not present in the string
#print(index_of_i)

sen ="This is string"
c= sen.count("s")
print(c)