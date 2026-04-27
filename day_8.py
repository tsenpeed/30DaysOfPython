# Exercises - Day 8

# 1
dog = {}
print(dog)

# 2
dog["name"] = "Bolt"
dog["color"] = "black"
dog["breed"] = "mixed"
dog["legs"] = 4
dog["age"] = 3
print(dog)

# 3
student = {
    "first_name": "Vinicius",
    "last_name": "Silva",
    "gender": "male",
    "age": 21,
    "marital_status": "single",
    "skills": ["Python", "HTML"],
    "country": "Brazil",
    "city": "Sao Paulo",
    "address": "Rua Exemplo, 123",
}
print(student)

# 4
print(len(student))

# 5
print(student["skills"])
print(type(student["skills"]))

# 6
student["skills"].extend(["CSS", "Git"])
print(student["skills"])

# 7
print(list(student.keys()))

# 8
print(list(student.values()))

# 9
print(list(student.items()))

# 10
student.pop("marital_status")
print(student)

# 11
del dog
