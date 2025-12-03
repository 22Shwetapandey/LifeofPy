"""course = ["History", "Civics", "Geography", "Math", "Physics", "Science"]
print(type(course))
print(course[1])
#using negative index
print(course[-2])
#slicing
print(course[0:5])
"""
#tuple example:
# tuple_1 =("Harry","Cory","Rachel","Emma")
# tuple_2 = tuple_1
# print(tuple_1)
# print(tuple_2)
# tuple_1[0]="Justin"
# print(tuple_1)
# print(tuple_2)


#sets
# set_1 = {"Harry", "Cory", "Rachel", "Emma"}
# print(set_1)
# print("Harry" in set_1)
# set_2= {"Harry", "Justin", "Rachel", "Emma"}
# print(set_1.intersection(set_2))
# print(set_1.difference(set_2))
# print(set_2.difference(set_1))
# print(set_1.union(set_2))
#
# #to create an empty set
# set_3 = set()
# print(set_3)

#dictonary, key value pair
# student = {"name": "john", "age": 25, "course":["math","compsci"]}
# print(student)
# #loop in dictonary
# for key, value in student.items():
#     print(key, value)

#Function
def student_info(*args, **kwargs): #accepting arbitary value
    print(args)
    print(kwargs)
student_info("Math","Art", name='John', age=25)


