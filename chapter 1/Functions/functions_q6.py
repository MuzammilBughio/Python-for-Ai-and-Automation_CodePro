# Use a lambda function inside map() to square all numbers in a list: [2, 4, 6, 8].

numbers = [2, 4, 6, 8]
square = list(map(lambda x: x**2 ,numbers))
print(square)

