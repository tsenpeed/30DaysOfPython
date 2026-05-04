from functools import reduce


"""
Exercises - Day 14
"""


def call_function(function, items):
    return function(items)


def get_string_lists(items):
    string_items = []

    for item in items:
        if type(item) == str:
            string_items.append(item)

    return string_items


def categorize_countries(countries):
    categories = {
        "land": [],
        "ia": [],
        "island": [],
        "stan": [],
    }

    for country in countries:
        lower_country = country.lower()

        if "land" in lower_country:
            categories["land"].append(country)
        if "ia" in lower_country:
            categories["ia"].append(country)
        if "island" in lower_country:
            categories["island"].append(country)
        if "stan" in lower_country:
            categories["stan"].append(country)

    return categories


def count_countries_by_first_letter(countries):
    counts = {}

    for country in countries:
        first_letter = country[0]
        if first_letter not in counts:
            counts[first_letter] = 0
        counts[first_letter] += 1

    return counts


def get_first_ten_countries(countries):
    return countries[:10]


def get_last_ten_countries(countries):
    return countries[-10:]


def most_spoken_languages(countries_data, number):
    languages = {}

    for country in countries_data:
        for language in country["languages"]:
            if language not in languages:
                languages[language] = 0
            languages[language] += 1

    sorted_languages = sorted(languages.items(), key=lambda item: item[1], reverse=True)
    return sorted_languages[:number]


def most_populated_countries(countries_data, number):
    populated_countries = []

    for country in countries_data:
        populated_countries.append((country["population"], country["name"]))

    populated_countries.sort(reverse=True)
    return populated_countries[:number]


# Level 1

# 1
# map changes each item in a list.
# filter keeps items that pass a condition.
# reduce combines all items into a single value.

# 2
# higher order function takes a function as a parameter or returns one.
# closure is a nested function that remembers the outer scope.
# decorator is a higher order function that wraps another function.

# 3
numbers = [1, 2, 3, 4, 5]

print(call_function(lambda items: list(map(lambda number: number * 2, items)), numbers))
print(call_function(lambda items: list(filter(lambda number: number % 2 == 0, items)), numbers))
print(call_function(lambda items: reduce(lambda total, number: total + number, items), numbers))

# 4
countries = ["Finland", "Sweden", "Norway", "Denmark", "Iceland"]

for country in countries:
    print(country)

# 5
names = ["Asabeneh", "David", "Donald", "Bill"]

for name in names:
    print(name)

# 6
numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    print(number)


# Level 2

# 1
upper_countries = list(map(lambda country: country.upper(), countries))
print(upper_countries)

# 2
square_numbers = list(map(lambda number: number ** 2, numbers))
print(square_numbers)

# 3
upper_names = list(map(lambda name: name.upper(), names))
print(upper_names)

# 4
countries_with_land = list(filter(lambda country: "land" in country.lower(), countries))
print(countries_with_land)

# 5
countries_with_six_characters = list(filter(lambda country: len(country) == 6, countries))
print(countries_with_six_characters)

# 6
countries_with_six_or_more_characters = list(filter(lambda country: len(country) >= 6, countries))
print(countries_with_six_or_more_characters)

# 7
countries_starting_with_e = list(filter(lambda country: country.startswith("E"), countries))
print(countries_starting_with_e)

# 8
land_countries_upper = list(map(lambda country: country.upper(), filter(lambda country: "land" in country.lower(), countries)))
print(land_countries_upper)

# 9
mixed_list = ["Asabeneh", 5, "Python", 10, True, "Finland", 3.14]
print(get_string_lists(mixed_list))

# 10
print(reduce(lambda total, number: total + number, numbers))

# 11
north_european_countries = ["Estonia", "Finland", "Sweden", "Denmark", "Norway", "Iceland"]
sentence = reduce(lambda total, country: total + ", " + country, north_european_countries[:-1])
sentence = sentence + ", and " + north_european_countries[-1] + " are north European countries"
print(sentence)

# 12
countries_for_categories = [
    "Finland",
    "Iceland",
    "Ireland",
    "Thailand",
    "Switzerland",
    "Pakistan",
    "Estonia",
    "India",
    "Nigeria",
    "Botswana",
    "Netherlands",
]
print(categorize_countries(countries_for_categories))

# 13
print(count_countries_by_first_letter(countries_for_categories))

# 14
print(get_first_ten_countries(countries_for_categories))

# 15
print(get_last_ten_countries(countries_for_categories))


# Level 3

try:
    from data.countries_data import countries_data
except ImportError:
    countries_data = [
        {"name": "China", "capital": "Beijing", "languages": ["Chinese"], "population": 1377422166},
        {"name": "India", "capital": "New Delhi", "languages": ["Hindi", "English"], "population": 1342512706},
        {"name": "United States", "capital": "Washington, D.C.", "languages": ["English"], "population": 331893745},
        {"name": "Indonesia", "capital": "Jakarta", "languages": ["Indonesian"], "population": 273523621},
        {"name": "Pakistan", "capital": "Islamabad", "languages": ["Urdu", "English"], "population": 220892331},
        {"name": "Brazil", "capital": "Brasilia", "languages": ["Portuguese"], "population": 213993437},
        {"name": "Nigeria", "capital": "Abuja", "languages": ["English"], "population": 206139587},
        {"name": "Bangladesh", "capital": "Dhaka", "languages": ["Bengali"], "population": 164689383},
        {"name": "Russia", "capital": "Moscow", "languages": ["Russian"], "population": 145934462},
        {"name": "Mexico", "capital": "Mexico City", "languages": ["Spanish"], "population": 128932753},
        {"name": "Finland", "capital": "Helsinki", "languages": ["Finnish", "Swedish"], "population": 5536146},
        {"name": "Sweden", "capital": "Stockholm", "languages": ["Swedish"], "population": 10353442},
        {"name": "Norway", "capital": "Oslo", "languages": ["Norwegian"], "population": 5372191},
        {"name": "Denmark", "capital": "Copenhagen", "languages": ["Danish"], "population": 5822763},
        {"name": "Iceland", "capital": "Reykjavik", "languages": ["Icelandic"], "population": 366425},
    ]

countries_by_name = sorted(countries_data, key=lambda country: country["name"])
countries_by_capital = sorted(countries_data, key=lambda country: country["capital"])
countries_by_population = sorted(countries_data, key=lambda country: country["population"])

print([country["name"] for country in countries_by_name[:10]])
print([country["capital"] for country in countries_by_capital[:10]])
print([country["population"] for country in countries_by_population[:10]])
print(most_spoken_languages(countries_data, 10))
print(most_populated_countries(countries_data, 10))
