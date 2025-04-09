# Write a program that:
# 1. Takes a string input from the user.
# 2. Reverses the string.
# 3. Checks if the original and reversed strings are the same (Palindrome check)

text = input("Enter a string: ").strip()

# Reverse the string
reversed_text = text[::-1]
print("Reversed String:", reversed_text)

# Check for palindrome
if text.lower() == reversed_text.lower():
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
