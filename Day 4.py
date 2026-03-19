# Day 4 - Program 7: Dictionaries

# Dictionary: stores data with labels (keys)
person = {
    "name": "Ravi",
    "age": 21,
    "city": "Coimbatore",
    "goal": "Agentic AI Engineer"
}

# Access values using keys
print(person["name"])
print(person["goal"])

# .get() is safer — returns None if key missing
print(person.get("salary", "not set yet"))

# Add or update a key
person["skills"] = ["Python", "LangChain"]
person["age"] = 22
print(person)

# Loop through dictionary
print("\nMy profile:")
for key, value in person.items():
    print(f"  {key}: {value}")

# This is what an AI API response looks like!
ai_response = {
    "model": "claude-sonnet",
    "message": "Hello! How can I help you today?",
    "tokens_used": 25,
    "success": True
}

print(f"\nAI said: {ai_response['message']}")
print(f"Tokens used: {ai_response['tokens_used']}")


# Day 4 - Program 8: Mini Project
# Student Report Card Generator

# Function to calculate grade
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

# Function to calculate average
def get_average(scores):
    return sum(scores) / len(scores)

# Function to print report
def print_report(student):
    print("\n" + "="*35)
    print(f"  REPORT CARD: {student['name'].upper()}")
    print("="*35)
    for subject, score in student["scores"].items():
        grade = get_grade(score)
        print(f"  {subject:12}: {score}  ({grade})")
    avg = get_average(list(student["scores"].values()))
    print(f"\n  Average    : {avg:.1f}")
    print(f"  Final Grade: {get_grade(avg)}")
    print("="*35)

# Student data
students = [
    {
        "name": "Ravi",
        "scores": {"Python": 92, "Maths": 85, "English": 78}
    },
    {
        "name": "Priya",
        "scores": {"Python": 88, "Maths": 95, "English": 91}
    }
]

# Print report for each student
for student in students:
    print_report(student)