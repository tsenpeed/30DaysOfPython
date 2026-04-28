greeting = "lol"
print(greeting[::-1])

# 1
space = " "
full_string_TDOP = 'Thirty' + space + 'Days' + space + 'Of' + space + 'Python'
print(full_string_TDOP)

# 2

full_string_CFA = 'Coding' + space + 'for' + space + 'All.'
print(full_string_CFA.swapcase())

# 3 4
xunga_variable = 'Xunga Company'
print(xunga_variable.swapcase(),full_string_CFA.capitalize())

# 5 

print(len(xunga_variable))

# 6 7 LUUULLEEEEII

print(xunga_variable.upper())
print(xunga_variable.lower())

# 8 

print(full_string_CFA.swapcase())
print(full_string_CFA.capitalize())
print(full_string_CFA.title())

# 9 

slice = full_string_CFA[7:]
print (slice)

# 10

if full_string_CFA.find('Coding') != -1:
    print ('Existe.')


# 11

print(full_string_CFA.replace('Coding','BILUNGERS'))

# 12

x = 'Python for Everyone'
print(x)
print(x.replace('Everyone','All'))

# 13


bungers = 'ahahaha' + space +'aajehhahaekkae' + space + 'isjdijfj8ewf98uef'
print(bungers.split(space))

# 14

socials = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(socials.split(', '))

# 15

print(full_string_CFA[0]) # first character is C at index 0 

# 16

print(full_string_CFA[-1])

# 17

print(full_string_CFA[10])

# 18

full_string_PFE = 'Python for Everyone'
print(full_string_PFE[0],full_string_PFE[7],full_string_PFE[11])

# 19

print (full_string_CFA[0],full_string_CFA[7],full_string_CFA[11])

# 20 21 22

print(full_string_CFA.find('C'))
print(full_string_CFA.find('f'))
full_string_CFAP = full_string_CFA.replace('All.', 'All') + ' People'
print(full_string_CFAP)
print(full_string_CFAP.rfind('l'))

# 23

sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))

# 24

sentence_2 = "You cannot end a sentence with because because because is a conjunction"
print(sentence_2.rfind('because'))

# 25

sentence_3 = "You cannot end a sentence with because because because is a conjunction"
print(sentence_3.replace('because','l'))

# 26

print(sentence_3.find('because'))

# 27

# same as 25

# 28

print(full_string_CFA.startswith('Coding'))

# 29

print(full_string_CFA.endswith('Coding'))

# 30

sentence_4 = '   Coding For All      '
print(sentence_4.strip()) # intended way
print(sentence_4.replace('   ','').replace('      ','') ) # noob way (how i would do it without my buddy copilot)

# 31

sentence_5 = '30DaysOfPython'
sentence_6 = 'thirty_days_of_python'
print(sentence_5.isidentifier())
print(sentence_6.isidentifier()) # this one

# 32

list_1 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# #'.join(list_1))

# 33

sentence_7 = """I am enjoying this challenge.
I just wonder what is next."""

print(sentence_7)

# had enough we go next


