# 1. Create two variables, a = 9 and b = 40, then write an expression to add them.

a = 9
b = 40

add = a + b
print(add)


# 2. What is the output of type(123) and type("123")?

print(type(123))      # <class 'int'>
print(type("123"))    # <class 'str'>


# 3. If ab = "2345" and cd = "3253", what happens when you write ab + cd?

ab = "2345"
cd = "3253"

print(ab + cd)        # 23453253 (String concatenation)


# 4. How do you convert ab and cd to integers before adding them?

add = int(ab) + int(cd)
print(add)


# 5. If name = "sahil", what does name.lower() return?

name = "sahil"
print(name.lower())   # sahil


# 6. What does name.count("a") return for name = "sahil"?

print(name.count("a"))   # 1


# 7. What is the result of len("Python")?

print(len("Python"))     # 6


# 8. What does "Notebook"[0:3] return?

print("Notebook"[0:3])   # Not


# 9. What does "Python"[1:-1] return?

print("Python"[1:-1])    # ytho


# 10. Evaluate 11 // 2 and 11 % 2

print(11 // 2)   # 5
print(11 % 2)    # 1


# 11. What is the value of 2 ** 3 ** 2 ?

print(2 ** 3 ** 2)   # 512


# 12. What is the result of 10 + 2 * 3, and why?

print(10 + 2 * 3)    # 16
# Multiplication has higher precedence than addition.


# 13. If a = 45 and b = 4, what are the results of a > b and a == b ?

a = 45
b = 4

print(a > b)     # True
print(a == b)    # False


# 14. If b1 = True and b2 = False, what do
# not(b1), b1 and b2, and b1 or b2 return?

b1 = True
b2 = False

print(not(b1))       # False
print(b1 and b2)     # False
print(b1 or b2)      # True


# 15. What does input() return by default in Python?

# input() returns data as a string by default.


# 16. Write a small program that takes two integer inputs and prints their sum.

a = int(input("Enter A: "))
b = int(input("Enter B: "))

print("Sum =", a + b)


# 17. Write an if-elif-else block that prints whether a number is positive, negative, or zero.

num = int(input("Enter Number To Check: "))

if num > 0:
    print("Number is Positive")

elif num < 0:
    print("Number is Negative")

else:
    print("Number is Zero")


# 18. What is the difference between if-elif-else and match-case?

# if-elif-else:
# Used for checking conditions and logical expressions.

# match-case:
# Used for pattern matching and comparing specific values.


# 19. Write a match-case function that returns the message for HTTP status code 404.

def fnc(code):
    match code:
        case 200:
            return "200 OK"

        case 404:
            return "404 Not Found"

        case 501:
            return "501 Not Implemented"

        case 600:
            return "600 Unknown Error"

        case _:
            return "Unknown"

print(fnc(404))


# 20. Use an f-string to print Python left-aligned,
# right-aligned, and center-aligned in a field of width 10.

print(f"{'Python':<10}")   # Left-align
print(f"{'Python':>10}")   # Right-align
print(f"{'Python':^10}")   # Center-align