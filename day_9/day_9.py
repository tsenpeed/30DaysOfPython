#jumped to day 9 out of boredom, will go back to day 6, 7, HAHAHAHAAH, 8 later i guess.
from datetime import datetime

# EEEEEEEEEEEEEEEEEEEEEEEEEEEExercises 

# 0N3

age = int(input("Type your age! (numbers only pleas) >>> "))

if age >= 18:
    print ('YOU ARE OLD ENOUGH TO DRIVE VRUMMM')

else:
    print ('CANT DRIVE SYBAUUU')

# TW0

your_age = int(input("ples typ ur age :) > > > "))

today = datetime.now()
birthday = datetime(2004, 11, 17)
my_age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

print(f"My age: {my_age}")
diff = my_age - your_age

if diff < 0:
    print(f'You are {abs(diff)} years older than me')

elif diff == 0:
    print ("We are same age :) ")

else:
    print (f"You are {abs(diff)} years younger than me")

# THR33

number_a = int(input("ples enter the first numba :) >>> "))
number_b = int(input("ples, enter the SECOND numba :) >>> "))
diff_numbers = number_a - number_b

if diff_numbers < 0:
    print(f'First number {number_a} is less than second number {number_b} ')

elif diff_numbers == 0:
    print ("They are the same ^_^ ")

else:
    print (f"First number {number_a} is greater than second number {number_b}")

# Next level 

# 0N3 

score = int(input("Type your score! (0-100) >>> "))

if score >= 90:
    print ('WOW, thats an A')
elif score < 90 and score >= 80:
    print ('thats an B lilbro')
elif score < 80 and score >= 70:
    print ('thats an C lilbro')
elif score < 70 and score >= 60:
    print ('thats an D lilbro')
else:
    print ('F in the chat, its an F!')



# TW0

month = input("Type a valid month in english : January, February, March, April, May, June, July, August, September, October, November, December >>> ")
if month in ['September', 'October', 'November']:
    print('The season is Autumn')
elif month in ['December', 'January', 'February']:
    print('The season is Winter')
elif month in ['March', 'April', 'May']:
    print('The season is Spring')
elif month in ['June', 'July', 'August']:
    print('The season is Summer')
else:
    print('Pls enter a valid month name')

# THR33

fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_input = input("Enter a fruit name >>> ")

if fruit_input in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit_input)
    print(fruits)



# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #