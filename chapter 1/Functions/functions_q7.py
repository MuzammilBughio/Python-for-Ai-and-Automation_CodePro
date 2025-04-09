# Use the reduce() function with a lambda to find the largest number in a list.

def my_reduce(func, iterable):
    result = iterable[0]
    for item in iterable[1:]:
        result = func(result, item)
    return result

numbers = [3, 10, 5, 8, 15, 2]

largest = my_reduce(lambda a, b: a if a > b else b, numbers)

print("Largest number:", largest)

