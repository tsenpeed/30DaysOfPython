# Exercises - Day 7

it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Level 1

# 1
print(len(it_companies))

# 2
it_companies.add("Twitter")
print(it_companies)

# 3
it_companies.update(["Netflix", "Tesla", "Intel"])
print(it_companies)

# 4
it_companies.remove("Intel")
print(it_companies)

# 5
print("remove raises an error if the item does not exist, discard does not.")

# Level 2

# 1
print(A.union(B))

# 2
print(A.intersection(B))

# 3
print(A.issubset(B))

# 4
print(A.isdisjoint(B))

# 5
A_with_B = A.union(B)
B_with_A = B.union(A)
print(A_with_B)
print(B_with_A)

# 6
print(A.symmetric_difference(B))

# 7
del A
del B

# Level 3

# 1
age_set = set(age)
print(len(age))
print(len(age_set))
print("The list is bigger." if len(age) > len(age_set) else "The set is bigger.")

# 2
print("string: ordered and immutable text data")
print("list: ordered and mutable collection")
print("tuple: ordered and immutable collection")
print("set: unordered collection of unique items")

# 3
sentence = "I am a teacher and I love to inspire and teach people."
cleaned_sentence = sentence.replace(".", "")
unique_words = set(cleaned_sentence.split())
print(unique_words)
print(len(unique_words))
