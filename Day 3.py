# Day 3 - Program 5: Loops

# for loop with range()
print("Counting 1 to 5:")
for i in range(1, 6):
    print(i)

# Loop through a list
months = ["March", "April", "May", "June", "July", "August"]
print("\nMy learning months:")
for month in months:
    print(f"  {month}")

# while loop — runs until condition is False
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count = count - 1
print("Go!")

# break: stop the loop early
print("\nStop at 3:")
for i in range(1, 10):
    if i == 3:
        break
    print(i)

# continue: skip one iteration
print("\nSkip 3:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

    # Day 3 - Program 6: Functions

# Basic function — no input, no output
def say_hello():
    print("Hello! Welcome to Python.")

say_hello()  # calling the function

# Function with parameters (inputs)
def greet(name, city):
    print(f"Hello {name}, from {city}!")

greet("Ravi", "Coimbatore")
greet("Priya", "Chennai")

# Function with return value
def add(a, b):
    result = a + b
    return result

answer = add(10, 25)
print(f"10 + 25 = {answer}")

# Function with default value
def introduce(name, role="student"):
    print(f"I am {name}, I am a {role}")

introduce("Ravi")                    # uses default "student"
introduce("Priya", "AI engineer")   # overrides default

# Practical function: check if someone is an adult
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

print(is_adult(21))   # True
print(is_adult(15))   # False