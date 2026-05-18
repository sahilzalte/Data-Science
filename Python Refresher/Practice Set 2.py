# =========================
# A. Loops
# =========================

# 1. Difference between for loop and while loop

# for loop:
# Used when the number of iterations is known.

# while loop:
# Used when the number of iterations is unknown
# and depends on a condition.


# 2. Write a for loop to print all numbers from 1 to 10

for i in range(1, 11):
    print(i)


# 3. Write a while loop that prints numbers from 5 to 1 in reverse order

count = 5

while count >= 1:
    print(count)
    count -= 1


# 4. Write a loop that prints all even numbers from 1 to 20

for i in range(1, 21):
    if i % 2 == 0:
        print(i)


# 5. Write a loop that skips the number 5 and stops when it reaches 10

for i in range(1, 11):

    if i == 5:
        continue

    if i == 10:
        break

    print(i)


# =========================
# B. Lists
# =========================

# 6. Create a list of five numbers and change the second element

num_list = [1, 2, 3, 4, 5]

num_list[1] = 50

print(num_list)


# 7. Use append() to add a new item to a list

num_list = [1, 2, 3, 4, 5]

num_list.append(56)

print(num_list)


# 8. Use extend() to merge two lists

num_list1 = [1, 2, 3, 4, 5]
num_list2 = [6, 7, 8, 9, 10]

num_list1.extend(num_list2)

print(num_list1)


# 9. Write code to insert a value at index 2 in a list

num_list = [1, 2, 3, 4, 5]

num_list.insert(2, 56)

print(num_list)


# 10. Sort a list in ascending order and print both the original and sorted versions

org_list = [54, 6, 3, 8, 2, 1]

print(f"Original List : {org_list}")

sorted_list = sorted(org_list)

print(f"Sorted List : {sorted_list}")


# =========================
# C. Tuples
# =========================

# 11. What is a tuple, and how is it different from a list?

# Tuple:
# A tuple is an ordered collection of items.

# Difference:
# Tuples are immutable (cannot be changed),
# while lists are mutable (can be changed).


# 12. Create a tuple with three items and print the second item

numbers = (1, 2, 3)

print(numbers[1])


# 13. Write code to unpack a tuple into three variables

numbers = ("Sahil", 89, 92.83)

name, roll_no, percentage = numbers

print(name)
print(roll_no)
print(percentage)


# 14. Create a single-element tuple and print its type

single_element = (10,)

print(single_element)
print(type(single_element))


# 15. Write code to use count() and index() on a tuple

numbers = (1, 4, 1, 4, 1, 1, 2, 3)

print(numbers.count(1))
print(numbers.index(2))


# =========================
# D. Sets
# =========================

# 16. Create a set from a list with duplicate values

set_value = set([1, 4, 1, 4, 1, 1, 2, 3])

print(set_value)


# 17. Add a new element to a set using add()

set_value = {1, 2, 3, 4, 5}

set_value.add(10)

print(set_value)


# 18. Use update() to add multiple items to a set

set_value = {1, 2, 3, 4, 5}

set_value.update([100, 56, 47, 98, 35])

print(set_value)


# 19. Write code to find the union of two sets and print the result

set1 = {1, 2, 3, 4, 5}
set2 = {6, 7, 8, 10}

union_set = set1.union(set2)

print(union_set)


# 20. Write code to find the intersection of two sets and print the result

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

intersection_set = set1.intersection(set2)

print(intersection_set)


# =========================
# E. Dictionaries
# =========================

# 21. What is a dictionary in Python?

# Dictionary:
# A dictionary is a collection of key-value pairs.


# 22. Create a dictionary for a student with name, age, and grade

student = {
    "name": "Sahil",
    "age": 19,
    "grade": "Fail"
}

print(student)


# 23. Access a value using a key and print it

print(student["name"])
print(student["age"])
print(student["grade"])


# 24. Use get() to access a missing key with a default value

print(student.get("age"))

print(student.get("height", "Not Given"))


# 25. Use update() to change one value and add one new key

student.update({
    "age": 20,
    "hobby": "Gaming"
})

print(student)


# =========================
# F. File Handling and JSON
# =========================

# 26. Write code to create a text file and write a line into it

file = open("example.txt", "w")

file.write("Hello This is Written in Python")

file.close()


# 27. Write code to read the contents of a text file using with open()

with open("example.txt", "r") as f:
    content = f.read()
    print(content)


# 28. Save a Python dictionary to a JSON file

import json

dict_data = {
    "name": "Sahil",
    "age": 19,
    "grade": "Fail"
}

with open("data.json", "w") as js:
    json.dump(dict_data, js)


# 29. Read a JSON file and convert it back into a Python object

with open("data.json", "r") as js:
    content = json.load(js)
    print(content)


# 30. Write code to append a new line to an existing file

file = open("example.txt", "a")

for i in range(1, 5):
    file.write("\nThis is Appended Text")

file.close()


# =========================
# Challenge Tasks
# =========================

# 1. Write a small program that uses a list, a loop, and a condition together

list_item = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in list_item:
    if item % 2 == 0:
        print(item)


# 2. Create a dictionary of student details and print all key-value pairs

student_dictionary = {
    "Name": "Sahil",
    "Age": 19,
    "Grade": "Fail",
    "Hobby": "Gamer"
}

for key, value in student_dictionary.items():
    print(key, ":", value)


# 3. Read and write a text file using with open()

with open("example.txt", "w") as f:
    f.write("Written Text")

with open("example.txt", "r") as f:
    print(f.read())


# 4. Convert a Python dictionary to JSON and back

import json

data = {
    "Name": "Sahil",
    "Age": 19,
    "Grade": "Fail",
    "Hobby": "Gamer"
}

with open("dictionary_data.json", "w") as file:
    json.dump(data, file)

with open("dictionary_data.json", "r") as file:
    converted_json = json.load(file)

print(converted_json)


# 5. Create a class with one attribute and one method

# Approach 1

class Student:

    def __init__(self):
        self.name = "Sahil"
        self.age = 19

    def info(self):
        print(self.name)
        print(self.age)


std = Student()

std.info()


# Approach 2

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name)
        print(self.age)


std = Student("Sahil", 19)

std.info()