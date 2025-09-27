from collections import Counter

# Our student records: list of dictionaries
students = [
    {"id": 1, "name": "Alice", "courses": ["Math", "Physics"]},
    {"id": 2, "name": "Bob", "courses": ["Biology", "Chemistry"]},
    {"id": 3, "name": "Charlie", "courses": ["Math", "Chemistry"]},
]

# 1. All student names
all_names = [s["name"] for s in students]

# 2. Courses for Bob (or any student you search for)
search_name = "Bob"
bob_courses = next(s["courses"] for s in students if s["name"] == search_name)

# 3. All unique courses offered
all_courses = {c for s in students for c in s["courses"]}

# 4. (Extra) Count how many times each course appears across all students
course_counts = Counter(c for s in students for c in s["courses"])

# Display results
print("Names:", all_names)
print(f"{search_name}'s courses:", bob_courses)
print("All courses offered:", all_courses)
print("Student count per course:", course_counts)
