import keyword


countries_data = [
    {"name": "China", "population": 1444216107, "languages": ["Chinese"]},
    {"name": "India", "population": 1393409038, "languages": ["Hindi", "English"]},
    {"name": "United States", "population": 331893745, "languages": ["English"]},
    {"name": "Indonesia", "population": 273523621, "languages": ["Indonesian"]},
    {"name": "Pakistan", "population": 220892331, "languages": ["Urdu", "English"]},
    {"name": "Brazil", "population": 213993437, "languages": ["Portuguese"]},
    {"name": "Nigeria", "population": 206139587, "languages": ["English"]},
    {"name": "Bangladesh", "population": 164689383, "languages": ["Bengali"]},
    {"name": "Russia", "population": 145934462, "languages": ["Russian"]},
    {"name": "Mexico", "population": 128932753, "languages": ["Spanish"]},
]


# Exercises - Day 11

# Level 1
def add_two_numbers(num_one, num_two):
    return num_one + num_two


def area_of_circle(radius):
    return 3.14 * radius * radius


def add_all_nums(*nums):
    total = 0

    for num in nums:
        if type(num) != int and type(num) != float:
            return "All items must be numbers."
        total += num

    return total


def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def check_season(month):
    month = month.lower()

    if month == "september" or month == "october" or month == "november":
        return "Autumn"
    elif month == "december" or month == "january" or month == "february":
        return "Winter"
    elif month == "march" or month == "april" or month == "may":
        return "Spring"
    elif month == "june" or month == "july" or month == "august":
        return "Summer"
    else:
        return "Invalid month"


def calculate_slope(x1, y1, x2, y2):
    if x2 - x1 == 0:
        return "Slope is undefined."
    return (y2 - y1) / (x2 - x1)


def solve_quadratic_eqn(a, b, c):
    d = b ** 2 - 4 * a * c

    if d < 0:
        return "No real solution"

    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)
    return x1, x2


def print_list(my_list):
    for item in my_list:
        print(item)


def reverse_list(my_list):
    reversed_list = []

    for i in range(len(my_list) - 1, -1, -1):
        reversed_list.append(my_list[i])

    return reversed_list


def capitalize_list_items(my_list):
    capitalized_list = []

    for item in my_list:
        capitalized_list.append(item.capitalize())

    return capitalized_list


def add_item(my_list, item):
    my_list.append(item)
    return my_list


def remove_item(my_list, item):
    if item in my_list:
        my_list.remove(item)
    return my_list


def sum_of_numbers(number):
    total = 0

    for i in range(number + 1):
        total += i

    return total


def sum_of_odds(number):
    total = 0

    for i in range(number + 1):
        if i % 2 != 0:
            total += i

    return total


def sum_of_even(number):
    total = 0

    for i in range(number + 1):
        if i % 2 == 0:
            total += i

    return total


# Level 2
def evens_and_odds(number):
    even_count = 0
    odd_count = 0

    for i in range(number + 1):
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return "The number of odds are " + str(odd_count) + ". The number of evens are " + str(even_count) + "."


def factorial(number):
    total = 1

    for i in range(1, number + 1):
        total *= i

    return total


def is_empty(item):
    if item:
        return False
    return True


def calculate_mean(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


def calculate_median(numbers):
    numbers.sort()
    middle = len(numbers) // 2

    if len(numbers) % 2 == 0:
        return (numbers[middle - 1] + numbers[middle]) / 2
    else:
        return numbers[middle]


def calculate_mode(numbers):
    values = []
    counts = []

    for number in numbers:
        if number not in values:
            values.append(number)
            counts.append(numbers.count(number))

    biggest_count = max(counts)
    modes = []

    for i in range(len(values)):
        if counts[i] == biggest_count:
            modes.append(values[i])

    return {"mode": modes, "count": biggest_count}


def calculate_range(numbers):
    return max(numbers) - min(numbers)


def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    total = 0

    for number in numbers:
        total += (number - mean) ** 2

    return total / len(numbers)


def calculate_std(numbers):
    return calculate_variance(numbers) ** 0.5


def greet(name="Guest"):
    return "Hello, " + name + "!"


def show_args(**args):
    text = "Received: "
    first = True

    for key, value in args.items():
        if first:
            text += str(key) + ": " + str(value)
            first = False
        else:
            text += ", " + str(key) + ": " + str(value)

    return text


# Level 3
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def are_all_items_unique(my_list):
    for item in my_list:
        if my_list.count(item) > 1:
            return False
    return True


def are_all_items_same_type(my_list):
    first_type = type(my_list[0])

    for item in my_list:
        if type(item) != first_type:
            return False

    return True


def is_valid_variable(variable):
    if variable.isidentifier() and not keyword.iskeyword(variable):
        return True
    return False


def most_spoken_languages(number):
    languages = []
    language_count = []

    for country in countries_data:
        for language in country["languages"]:
            if language not in languages:
                languages.append(language)

    for language in languages:
        count = 0
        for country in countries_data:
            if language in country["languages"]:
                count += 1
        language_count.append((count, language))

    language_count.sort(reverse=True)
    return language_count[:number]


def most_populated_countries(number):
    populated_countries = []

    for country in countries_data:
        populated_countries.append((country["population"], country["name"]))

    populated_countries.sort(reverse=True)
    return populated_countries[:number]


print("Level 1")
print(add_two_numbers(2, 3))
print(area_of_circle(10))
print(add_all_nums(1, 2, 3, 4, 5))
print(convert_celsius_to_fahrenheit(30))
print(check_season("March"))
print(calculate_slope(1, 2, 3, 6))
print(solve_quadratic_eqn(1, -3, 2))
print_list([1, 2, 3])
print(reverse_list([1, 2, 3, 4, 5]))
print(capitalize_list_items(["apple", "banana", "mango"]))
print(add_item(["Potato", "Tomato"], "Milk"))
print(remove_item(["Potato", "Tomato", "Milk"], "Tomato"))
print(sum_of_numbers(10))
print(sum_of_odds(10))
print(sum_of_even(10))

print("\nLevel 2")
print(evens_and_odds(100))
print(factorial(5))
print(is_empty([]))
sample_numbers = [1, 2, 2, 3, 4, 5]
print(calculate_mean(sample_numbers))
print(calculate_median(sample_numbers))
print(calculate_mode(sample_numbers))
print(calculate_range(sample_numbers))
print(calculate_variance(sample_numbers))
print(calculate_std(sample_numbers))
print(greet())
print(greet("Alice"))
print(show_args(name="Alice", age=30, city="New York"))

print("\nLevel 3")
print(is_prime(29))
print(are_all_items_unique([1, 2, 3, 4]))
print(are_all_items_same_type([1, 2, 3]))
print(is_valid_variable("first_name"))
print(most_spoken_languages(5))
print(most_populated_countries(5))
