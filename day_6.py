# Exercises - Day 6

# Level 1

# 1
empty_tuple = ()
print(empty_tuple)

# 2
sisters = ("Ana", "Bia", "Clara")
brothers = ("Leo", "Caio", "Davi")
print(sisters)
print(brothers)

# 3
siblings = sisters + brothers
print(siblings)

# 4
print(len(siblings))

# 5
family_members = siblings + ("Maria", "Carlos")
print(family_members)

# Level 2

# 1
sister_1, sister_2, sister_3, brother_1, brother_2, brother_3, mother, father = family_members
print((sister_1, sister_2, sister_3))
print((brother_1, brother_2, brother_3))
print((mother, father))

# 2
fruits = ("banana", "orange", "mango", "lemon")
vegetables = ("tomato", "potato", "cabbage", "onion", "carrot")
animal_products = ("milk", "cheese", "butter", "egg")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# 3
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# 4
middle_index = len(food_stuff_lt) // 2
if len(food_stuff_lt) % 2 == 0:
    middle_items = food_stuff_lt[middle_index - 1:middle_index + 1]
else:
    middle_items = [food_stuff_lt[middle_index]]
print(middle_items)

# 5
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])

# 6
del food_stuff_tp

# 7
nordic_countries = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)
