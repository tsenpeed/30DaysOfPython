fruits = ['banana', 'orange', 'mango', 'lemon']
print (fruits[0])

orange_finder = fruits.index('orange')
print (orange_finder)
print (fruits[orange_finder])
print (fruits)

last_index = len(fruits) - 1
print (fruits[last_index])
fruits[last_index] = 'abacaxi'


print (fruits)

lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']

# 1 

empty_list = [ ]
print (empty_list)

# 2 

six_list= ['bunga','xunga','dunga','lunga','bilunga',"xilumbra"]
print (six_list)

# 3 

print (len(six_list))

# 4

print (six_list[0])
print (six_list[-1])
middle_six_list = len(six_list) // 2
print (six_list[middle_six_list])

# 5

mixed_data_types = ['Vinicius', 21, 165, 'single', 'no']
print (mixed_data_types)

# 6 

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print (it_companies)

# 7 

# already did

# 8 

print (len(it_companies))

# 9 

print (it_companies [0])
print (it_companies[-1])
middle_it_companies = len(it_companies) // 2
print (it_companies[middle_it_companies])

# 10

it_companies[0] = 'Meta'
print (it_companies)

# 11 

it_companies.append('Dell') 
print (it_companies[-1])

# 12


middle_it_companies = len(it_companies) // 2

it_companies.insert(middle_it_companies, 'Samsung')
print (it_companies)

# 13

it_companies[3] = it_companies[3].upper()
print (it_companies[3])



# 14

joined_companies = '#' + ' #'.join(it_companies)
print (joined_companies)

# 15


x = input("Enter a company name: ")
if x in it_companies:
    print (x + " is found")

else:
    print (x + " is not found")

# 16

it_companies.sort()
print (it_companies)

# 17

it_companies.reverse()
print (it_companies)

# 18

it_companies2 = it_companies[3:-3]
print (it_companies2)

middle_it_companies2 = len(it_companies2) // 2
it_companies2 = it_companies.pop(middle_it_companies2)
print (it_companies2)

# 19 



