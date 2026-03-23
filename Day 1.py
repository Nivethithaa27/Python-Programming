# Day 1 - Program 1: Hello World
# Variables store information

name = "Nivethitha"
age = 21
city = "Sathyamangalam"
favourite_food = "Briyani"
favourite_sport = "cricket"

# print() shows output on screen
print("Hello World!")
print("My name is", name)
print("I am", age, "years old")
print("I live in", city)
print("I love to eat",favourite_food)
print("I like to watch",favourite_sport)

# f-string: cleaner way to print variables
print(f"Hello! I am {name}, {age} years old girl from {city}.I love to eat {favourite_food} and Like to watch {favourite_sport}")


# Day 1 - Program 2: Data Types

# String = text (always in quotes)
my_name = "Nivethitha"
my_city = "sathyamangalam"

# Integer = whole number (no quotes)
my_age = 21
my_score = 95

# Float = decimal number
my_height = 5.9
my_gpa = 8.5

# Boolean = True or False only
is_student = True
has_job = False

# type() tells you what type a variable is
print(type(my_name))
print(type(my_age))
print(type(my_height))
print(type(is_student))

# Simple calculator using variables
num1 = 10
num2 = 3
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")
