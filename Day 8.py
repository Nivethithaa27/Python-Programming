person = {
    'Name': 'Nivethitha',
    'Age': 21,
    'City': 'Sathyamangalam',
    'ditrict': 'Erode',
    'State': 'Tamil Nadu',
    'Country': 'India',
    'Goal': 'Agentic AI Engineer',
    'Skills': ['Python', 'LLM', 'Machine Learning']
}
print(person['Name'])
print(person['Goal'])
print(person['Skills'])
print(person.get('Grade', 'Not available'))
for key,values in person.items():
    print(f'{key}: {values}')

friends = [
    {"name": "swetha", "age": 23, "place": "Erode"},
    {"name": "gomu", "age": 22, "place": "Coimbatore"},
    {"name": "lali", "age": 23, "place": "gobichettipalayam"},
]

for friend in friends:
    print(f"{friend['name']} is {friend['age']} years old and lives in {friend['place']}.")
person.update({"hobby": "doing reels"})
person.pop("State", None)
print(person)