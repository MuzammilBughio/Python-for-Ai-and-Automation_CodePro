#Write a function that takes a list of numbers and returns the sum of only the even numbers.

def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

numbers = list(map(int, input("Enter numbers : ").split()))

print("Sum of even numbers:", sum_even_numbers(numbers))



