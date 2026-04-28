import keyword
import math
from collections import Counter


COUNTRIES_DATA = [
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
    {"name": "Japan", "population": 125836021, "languages": ["Japanese"]},
    {"name": "Ethiopia", "population": 120283026, "languages": ["Amharic"]},
]


# Exercises - Day 11


# Level 1
def add_two_numbers(num_one, num_two):
    return num_one + num_two


def area_of_circle(radius):
    return math.pi * radius * radius


def add_all_nums(*nums):
    if not nums:
        return 0

    total = 0
    for num in nums:
        if not isinstance(num, (int, float)):
            return "All items must be numbers."
        total += num
    return total


def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def check_season(month):
    month = month.strip().lower()
    if month in {"september", "october", "november"}:
        return "Autumn"
    if month in {"december", "january", "february"}:
        return "Winter"
    if month in {"march", "april", "may"}:
        return "Spring"
    if month in {"june", "july", "august"}:
        return "Summer"
    return "Invalid month"


def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError("Slope is undefined for a vertical line.")
    return (y2 - y1) / (x2 - x1)


def solve_quadratic_eqn(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero.")

    discriminant = (b ** 2) - (4 * a * c)
    if discriminant >= 0:
        sqrt_discriminant = math.sqrt(discriminant)
    else:
        sqrt_discriminant = complex(0, math.sqrt(-discriminant))

    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)
    return x1, x2


def print_list(items):
    for item in items:
        print(item)


def reverse_list(items):
    reversed_items = []
    for index in range(len(items) - 1, -1, -1):
        reversed_items.append(items[index])
    return reversed_items


def capitalize_list_items(items):
    return [str(item).capitalize() for item in items]


def add_item(items, item):
    updated_items = items[:]
    updated_items.append(item)
    return updated_items


def remove_item(items, item):
    updated_items = items[:]
    if item in updated_items:
        updated_items.remove(item)
    return updated_items


def sum_of_numbers(number):
    return sum(range(number + 1))


def sum_of_odds(number):
    return sum(value for value in range(number + 1) if value % 2 != 0)


def sum_of_even(number):
    return sum(value for value in range(number + 1) if value % 2 == 0)


# Level 2
def evens_and_odds(number):
    even_count = 0
    odd_count = 0

    for value in range(number + 1):
        if value % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return f"The number of odds are {odd_count}. The number of evens are {even_count}."


def factorial(number):
    if number < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")

    total = 1
    for value in range(2, number + 1):
        total *= value
    return total


def is_empty(value):
    return not bool(value)


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    length = len(sorted_numbers)
    midpoint = length // 2

    if length % 2 == 0:
        return (sorted_numbers[midpoint - 1] + sorted_numbers[midpoint]) / 2
    return sorted_numbers[midpoint]


def calculate_mode(numbers):
    counts = Counter(numbers)
    highest_count = max(counts.values())
    modes = [number for number, count in counts.items() if count == highest_count]
    return {"mode": modes, "count": highest_count}


def calculate_range(numbers):
    return max(numbers) - min(numbers)


def calculate_variance(numbers):
    mean = calculate_mean(numbers)
    squared_differences = [(number - mean) ** 2 for number in numbers]
    return sum(squared_differences) / len(numbers)


def calculate_std(numbers):
    return math.sqrt(calculate_variance(numbers))


def greet(name="Guest"):
    return f"Hello, {name}!"


def show_args(**kwargs):
    if not kwargs:
        return "Received:"
    pairs = [f"{key}: {value}" for key, value in kwargs.items()]
    return "Received: " + ", ".join(pairs)


# Level 3
def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False

    limit = int(math.sqrt(number)) + 1
    for divisor in range(3, limit, 2):
        if number % divisor == 0:
            return False
    return True


def are_all_items_unique(items):
    return len(items) == len(set(items))


def are_all_items_same_type(items):
    if not items:
        return True
    first_type = type(items[0])
    return all(isinstance(item, first_type) for item in items)


def is_valid_variable(variable_name):
    return variable_name.isidentifier() and not keyword.iskeyword(variable_name)


def most_spoken_languages(count=10, countries_data=None):
    countries_data = countries_data or COUNTRIES_DATA
    language_counts = Counter()

    for country in countries_data:
        for language in country["languages"]:
            language_counts[language] += 1

    return language_counts.most_common(count)


def most_populated_countries(count=10, countries_data=None):
    countries_data = countries_data or COUNTRIES_DATA
    sorted_countries = sorted(
        countries_data,
        key=lambda country: country["population"],
        reverse=True,
    )
    return [
        (country["name"], country["population"])
        for country in sorted_countries[:count]
    ]


if __name__ == "__main__":
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
    print(capitalize_list_items(["apple", "banana", "cherry"]))
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
