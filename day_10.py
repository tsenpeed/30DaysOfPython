# Exercises - Day 10

# Level 1

# 1
for number in range(11):
    print(number)

count = 0
while count <= 10:
    print(count)
    count += 1

# 2
for number in range(10, -1, -1):
    print(number)

count = 10
while count >= 0:
    print(count)
    count -= 1

# 3
for i in range(1, 8):
    print("#" * i)

# 4
for _ in range(8):
    row = ""
    for _ in range(8):
        row += "# "
    print(row.rstrip())

# 5
for number in range(11):
    print(f"{number} x {number} = {number * number}")

# 6
techs = ["Python", "Numpy", "Pandas", "Django", "Flask"]
for tech in techs:
    print(tech)

# 7
for number in range(101):
    if number % 2 == 0:
        print(number)

# 8
for number in range(101):
    if number % 2 != 0:
        print(number)

# Level 2

# 1
total = 0
for number in range(101):
    total += number
print(f"The sum of all numbers is {total}.")

# 2
even_sum = 0
odd_sum = 0
for number in range(101):
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number
print(f"The sum of all evens is {even_sum}. And the sum of all odds is {odd_sum}.")

# Level 3

# 1
countries = [
    "Finland",
    "Iceland",
    "Thailand",
    "Ireland",
    "Brazil",
    "Poland",
    "Switzerland",
]

countries_with_land = []
for country in countries:
    if "land" in country.lower():
        countries_with_land.append(country)
print(countries_with_land)

# 2
fruits = ["banana", "orange", "mango", "lemon"]
reversed_fruits = []
for index in range(len(fruits) - 1, -1, -1):
    reversed_fruits.append(fruits[index])
print(reversed_fruits)

# 3
countries_data = [
    {"name": "China", "population": 1444216107, "languages": ["Chinese"]},
    {"name": "India", "population": 1393409038, "languages": ["Hindi", "English"]},
    {"name": "United States", "population": 331893745, "languages": ["English"]},
    {"name": "Indonesia", "population": 273523621, "languages": ["Indonesian"]},
    {"name": "Brazil", "population": 213993437, "languages": ["Portuguese"]},
    {"name": "Pakistan", "population": 220892331, "languages": ["Urdu", "English"]},
    {"name": "Nigeria", "population": 206139587, "languages": ["English"]},
    {"name": "Bangladesh", "population": 164689383, "languages": ["Bengali"]},
    {"name": "Russia", "population": 145934460, "languages": ["Russian"]},
    {"name": "Mexico", "population": 128932753, "languages": ["Spanish"]},
]

all_languages = set()
language_count = {}
for country in countries_data:
    for language in country["languages"]:
        all_languages.add(language)
        language_count[language] = language_count.get(language, 0) + 1

print(len(all_languages))

most_spoken_languages = sorted(language_count.items(), key=lambda item: item[1], reverse=True)[:10]
print(most_spoken_languages)

most_populated_countries = sorted(
    countries_data,
    key=lambda country: country["population"],
    reverse=True,
)[:10]
print([(country["name"], country["population"]) for country in most_populated_countries])
