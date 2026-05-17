# Loops

# 1.
# for i in range(1,11):
#     print(i)

# 2.
# count = 5
# while count >=1:
#     print(count)
#     count -=1

# 3.
# for i in range (1,20):
#     if i %2==0:
#         print(i)

# 4.
# for i in range(1,10):
#     if i ==5:
#         continue
#     print(i)

# List

# 1.

# num_list = [1,2,3,4,5]
# num_list[1]=5
# print(num_list)

# 2.
# num_list = [1,2,3,4,5]
# num_list.append(56)
# print(num_list)

# 3.
# num_list1 = [1,2,3,4,5]
# num_list2 = [6,7,8,9,10]
# l = num_list1.extend(num_list2)
# print(num_list1)

# 4.
# num_list = [1,2,3,4,5]
# num_list.insert(1,56)
# print(num_list)

# 5.
# org_list = [54,6,3,8,2,1]
# print(f"Original List : {org_list}")
# org_list.sort()
# print(f"Sorted List : {org_list}")

# Tuples

# 1.
# numbers = (1, 2, 3)
# print(numbers[1])

# 2.
# numbers = ("Sahil",89,92.83)
# name,roll_no,percentage=numbers
# print(name)
# print(roll_no)
# print(percentage)

# 3.
# single_element=(10,)
# print(single_element)

# 4.
# numbers = (1,4,1,4,1,1,2, 3)
# print(numbers.count(1))
# print(numbers.index(2))

# Sets

# 1.
# set_value = set([1,4,1,4,1,1,2,3])
# print(set_value)

# 2.
# set_value = {1, 2, 3, 4, 5}
# set_value.add(10)
# print(set_value)

# 3.
# set_value = {1, 2, 3, 4, 5}
# set_value.update([100,56,47,98,35])
# print(set_value)

# 4.
# set1 = {1, 2, 3, 4, 5}
# set2 = {6, 7, 8, 10}
# union_set=set1.union(set2)
# print(union_set)

# 5
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# interSection = set1.intersection(set2)
# print(interSection)

# Dictionaries

# 1.
# Student  = {
#     "name":"Sahil",
#     "age":19,
#     "grade":"Fail"
# }

# 2
# Student  = {
#     "name":"Sahil",
#     "age":19,
#     "grade":"Fail"
# }
# print(Student["name"])
# print(Student["age"])
# print(Student["grade"])

# 3
# Student  = {
#     "name":"Sahil",
#     "age":19,
#     "grade":"Fail"
# }
# print(Student.get("age"))
# print(Student.get("height","Not Given"))

# 4.
# dict1 = {
#     "name":"Sahil",
#     "age":19,
#     "grade":"Fail"
# }
# dict1.update(
#     {
#         "age":19,
#         "Hobby":"Game"
#     }
# )
# print(dict1)

# File Handling ANd JSON
# 1.
# file = open("example.txt", "w")
# file.write("Hello This is Written in Python")

# 2.
# with open("example.txt","r") as f:
#     content  = f.read()
#     print(content)

# 3
# import json

# dict_data={
#     "name":"Sahil",
#     "age":19,
#     "grade":"Fail"
# }

# with open("data.json","w") as js:
#     json.dump(dict_data,js)

# 4.
# import json
# with open("data.json","r") as js:
#     content = json.load(js)
#     print(content)

# 5.
# file = open("example.txt", "a")
# for i in range(1,50):
#     file.write('\n This is Appended Text')
# file.close()

# Extra

# 1
# list_item = [1,2,3,4,5,6,7,8,9,10]

# for item in list_item:
#     if item % 2 ==0:
#         print(item)

# 2.
# Student_dictionary = {
#     "Name":"Sahil",
#     "Age":19,
#     "Grade":"Fail",
#     "Hobby":"Gamer"
# }
# print(f'keys : {Student_dictionary.keys()}')
# print(f'Values : {Student_dictionary.values()}')
# print(f'Both Keys And Values : {Student_dictionary}')

# 3.
# with open("example.txt","w") as f:
#     f.write("Writed Text")
# with open("example.txt","r") as f:
#     print(f.read())

# 4. 
# import json
# data={
#     "Name":"Sahil",
#     "Age":19,
#     "Grade":"Fail",
#     "Hobby":"Gamer"
# }
# file = open('dictionary_data.json',"w")
# json.dump(data,file)
# file.close()
# file = open('dictionary_data.json',"r")
# conveted_json = json.load(file)
# print(conveted_json)

# 5.
# Create a class with one attribute and one method
# Approch 1
# class Student:
#     def __init__(self):
#         self.name = "Sahil"
#         self.age = 19

#     def info(data,name,age):
#         print(data.name)
#         print(data.age)

# std = Student()
# std.info("Admin",34)

# # Approch 2
# class Student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def info(self):
#         print(self.name)
#         print(self.age)

# std = Student("Sahil",19)
# std.info()