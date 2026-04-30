"""
Exercises - Day 13
"""

# Level 1

# 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative_and_zero = [number for number in numbers if number <= 0]
print(negative_and_zero)

# 2
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [number for row in list_of_lists for number in row]
print(flattened_list)

# 3
tuples_list = [(i, i ** 0, i, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(tuples_list)

# 4
countries = [[("Finland", "Helsinki")], [("Sweden", "Stockholm")], [("Norway", "Oslo")]]
flattened_countries = [[country.upper(), country[:3].upper(), city.upper()] for [(country, city)] in countries]
print(flattened_countries)

# 5
countries_dictionary = [{"country": country.upper(), "city": city.upper()} for [(country, city)] in countries]
print(countries_dictionary)

# 6
names = [[("Asabeneh", "Yetayeh")], [("David", "Smith")], [("Donald", "Trump")], [("Bill", "Gates")]]
full_names = [first_name + " " + last_name for [(first_name, last_name)] in names]
print(full_names)

# 7
calculate_slope = lambda x1, y1, x2, y2: "Slope is undefined." if x2 - x1 == 0 else (y2 - y1) / (x2 - x1)
calculate_y_intercept = lambda m, x, y: y - m * x

print(calculate_slope(2, 2, 6, 10))
print(calculate_y_intercept(2, 3, 8))
