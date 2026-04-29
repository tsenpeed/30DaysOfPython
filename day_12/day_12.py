import random
import string


def random_user():
    all_chars = string.ascii_letters + string.digits
    user = "".join(random.choices(all_chars, k=6))
    return user

print(random_user())

# 2

def user_id_gen_by_user():
    
    all_chars = string.ascii_letters + string.digits
    
    x = int(input ("Numero de usuarios criados: "))
    y = int(input ("Numero de letras: "))
    
    for i in range (x):
        user = "".join(random.choices(all_chars, k=y))
        print(user)

user_id_gen_by_user()

# 3

def rgb_generator():

      for i in range(3):
          number = random.randint(0, 255)
          if i == 0:
              print("RED:", number)
          if i == 1:
              print("GREEN:", number)
          if i == 2:
              print("BLUE:", number)

rgb_generator()

# extra

def hexa_colors():  
    hexa_chars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = "".join(random.choices(hexa_chars, k=6))
    print ("#",color)

hexa_colors()

# Level 2 

# 1 

def list_of_hexa_colors(total):
    hexa_chars = "0123456789abcdef"
    colors = []

    for _ in range(total):
        color = "#" + "".join(random.choices(hexa_chars, k=6))
        colors.append(color)

    return colors

print(list_of_hexa_colors(3))

# 2

def list_of_rgb_colors(total):
    colors = []

    for _ in range(total):
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        colors.append(f"rgb({red}, {green}, {blue})")

    return colors

print(list_of_rgb_colors(3))

# 3

def generate_colors(color_type, total):
    colors = []

    if color_type == "hexa":
        for _ in range(total):
            color = "#" + "".join(random.choices("0123456789abcdef", k=6))
            colors.append(color)
    elif color_type == "rgb":
        for _ in range(total):
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            colors.append(f"rgb({red}, {green}, {blue})")

    return colors

print(generate_colors("hexa", 3))
print(generate_colors("rgb", 3))

# Level 3

# 1

def shuffle_list(items):
    shuffled_items = items[:]
    random.shuffle(shuffled_items)
    return shuffled_items

print(shuffle_list([1, 2, 3, 4, 5]))

# 2

def unique_random_numbers():
    return random.sample(range(10), 7)

print(unique_random_numbers())

