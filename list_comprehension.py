fruits = ["apple", "orange", "banana", "peach"]

# get first char of fruit with simple list comprehension
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)

# get first char of fruit for specific fruit with list comprehension
fruit_chars2 = [fruit[0] for fruit in fruits if fruit in ('apple', 'banana')]
print(fruit_chars2)
