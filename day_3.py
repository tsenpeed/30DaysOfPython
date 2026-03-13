# Exercises - Day 3

# 1 2 and 3
age = 21 #integer
height = 1.60 #meters and float
complex_number = 2 + 3j 

# 4 

height_triangle = int(input("Enter the height of the triangle: "))
base_triangle = int(input("Enter the base of the triangle: "))
area_triangle = height_triangle * base_triangle * 0.5 
print("The area of the triangle is ",area_triangle)

# 5
side_a = int(input("Enter side a of the triangle: "))
side_b = int(input("Enter side b of the triangle: "))
side_c = int(input("Enter side c of the triangle: "))
perimeter_triangle = side_a + side_b + side_c
print("The perimeter of the triangle is ",perimeter_triangle)

# 6
length_rectangle = int(input("Enter the length of the rectangle: "))
width_rectangle = int(input("Enter the width of the rectangle: "))
area_rectangle = length_rectangle * width_rectangle
perimeter_rectangle = 2 * (length_rectangle + width_rectangle)
print("The area of the rectangle is ",area_rectangle)
print("The perimeter of the rectangle is ",perimeter_rectangle)

# 7

radius_circle = int(input("Enter the radius of the circle: "))
pi = 3.14
area_circle = pi * radius_circle ** 2
circumference_circle = 2 * pi * radius_circle
print("The area of the circle is ",area_circle)
print("The circumference of the circle is ",circumference_circle)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2
x_intercept = 1  # y = 0 => 0 = 2x - 2 => x = 1
y_intercept = -2  # x = 0 => y = -2
print("\n--- Exercise 8 ---")
print(f"Equation: y = 2x - 2")
print(f"Slope: {m}")
print(f"x-intercept: {x_intercept}")
print(f"y-intercept: {y_intercept}")

# 9. Slope and Euclidean distance between (2,2) and (6,10)
from math import sqrt
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_points = (y2 - y1) / (x2 - x1)
distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("\n--- Exercise 9 ---")
print(f"Slope between points (2,2) and (6,10): {slope_points}")
print(f"Euclidean distance: {distance}")

# 10. Compare the slopes in tasks 8 and 9
print("\n--- Exercise 10 ---")
print(f"Slope from exercise 8: {m}")
print(f"Slope from exercise 9: {slope_points}")
print(f"Are they equal? {m == slope_points}")

# 11. Calculate y = x^2 + 6x + 9, find x where y = 0
print("\n--- Exercise 11 ---")
print("y = x^2 + 6x + 9")
for x in range(-10, 11):
    y = x**2 + 6*x + 9
    if y == 0:
        print(f"y is zero when x = {x}")

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison
print("\n--- Exercise 12 ---")
python_len = len('python')
dragon_len = len('dragon')
print(f"Length of 'python': {python_len}")
print(f"Length of 'dragon': {dragon_len}")
print(f"Are they equal? {python_len == dragon_len}")

# 13. Use 'and' operator to check if 'on' is found in both 'python' and 'dragon'
print("\n--- Exercise 13 ---")
result_13 = 'on' in 'python' and 'on' in 'dragon'
print(f"Is 'on' in both 'python' and 'dragon'? {result_13}")

# 14. Use 'in' operator to check if 'jargon' is in the sentence
print("\n--- Exercise 14 ---")
sentence = 'I hope this course is not full of jargon.'
result_14 = 'jargon' in sentence
print(f"Sentence: {sentence}")
print(f"Is 'jargon' in the sentence? {result_14}")

# 15. There is no 'on' in both dragon and python
print("\n--- Exercise 15 ---")
result_15 = 'on' not in 'dragon' and 'on' not in 'python'
print(f"There is no 'on' in both 'dragon' and 'python': {result_15}")

# 16. Find the length of 'python' and convert to float and string
print("\n--- Exercise 16 ---")
python_length = len('python')
python_float = float(python_length)
python_str = str(python_float)
print(f"Length of 'python': {python_length}")
print(f"As float: {python_float}")
print(f"As string: {python_str}")

# 17. Check if a number is even
print("\n--- Exercise 17 ---")
num = 4
is_even = num % 2 == 0
print(f"Is {num} even? {is_even}")

# 18. Check if floor division of 7 by 3 equals int(2.7)
print("\n--- Exercise 18 ---")
result_18 = 7 // 3 == int(2.7)
print(f"Floor division of 7 by 3: {7 // 3}")
print(f"int(2.7): {int(2.7)}")
print(f"Are they equal? {result_18}")

# 19. Check if type of '10' equals type of 10
print("\n--- Exercise 19 ---")
result_19 = type('10') == type(10)
print(f"Type of '10': {type('10')}")
print(f"Type of 10: {type(10)}")
print(f"Are they equal? {result_19}")

# 20. Check if int('9.8') equals 10
print("\n--- Exercise 20 ---")
try:
    result_20 = int(float('9.8')) == 10
    print(f"int(float('9.8')): {int(float('9.8'))}")
    print(f"Equals 10? {result_20}")
except ValueError:
    print("Cannot convert '9.8' directly to int. Use float('9.8') first.")

# 21. Prompt user for hours and rate per hour, calculate pay
print("\n--- Exercise 21 ---")
hours = float(input('Enter hours: '))
rate = float(input('Enter rate per hour: '))
weekly_earning = hours * rate
print(f'Your weekly earning is {weekly_earning}')

# 22. Prompt user for years, calculate seconds lived
print("\n--- Exercise 22 ---")
years = int(input('Enter number of years you have lived: '))
seconds = years * 365 * 24 * 60 * 60
print(f'You have lived for {seconds} seconds.')

# 23. Display the table
print("\n--- Exercise 23 ---")
for i in range(1, 6):
    row = f"{i} 1 {i} {i**2} {i**3}"
    print(row)

