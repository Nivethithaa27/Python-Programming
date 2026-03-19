# Day 2 - Program 3: Strings

Dream_job = "i want to become an agentic ai engineer"

# .upper() converts to UPPERCASE
print(Dream_job.upper())

# .title() capitalises First Letter Of Each Word
print(Dream_job.title())

# len() counts characters
print(f"Length: {len(Dream_job)} characters")

# .replace() swaps one word for another
new_sentence = Dream_job.replace("agentic ai", "Python")
print(new_sentence)

# Slicing: get part of a string
# [start:end] — end is not included
word = "Coimbatore"
print(word[0:4])   # prints "Coim"
print(word[4:])    # prints "batore"
print(word[-3:])   # prints last 3 letters

# .split() breaks string into a list
words = Dream_job.split()
print(words)
print(f"Word count: {len(words)}")


# Day 2 - Program 4: Lists

# A list stores multiple items
skills = ["Python", "LangChain", "LangGraph", "CrewAI"]

# Access by index (starts at 0)
print(skills[0])   # Python
print(skills[-1])  # CrewAI (last item)

# .append() adds to the end
skills.append("FastAPI")
print(skills)

# .remove() deletes an item
skills.remove("LangChain")
print(skills)

# len() counts items
print(f"I am learning {len(skills)} skills")

# Loop through a list
print("\nMy skills:")
for skill in skills:
    print(f"  - {skill}")

# List of numbers
scores = [85, 92, 78, 95, 88]
print(f"\nHighest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
print(f"Average: {sum(scores) / len(scores)}")
