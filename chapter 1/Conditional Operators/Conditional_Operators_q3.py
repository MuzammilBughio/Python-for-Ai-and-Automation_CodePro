# Compare the length of two strings.

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) > len(str2):
    print("The first string is longer.")
elif len(str1) < len(str2):
    print("The second string is longer.")
else:
    print("Both strings have the same length.")
