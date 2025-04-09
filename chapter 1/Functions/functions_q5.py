# Write a function reverse_string(s) that takes a string and returns it in reverse.

def reverse_string(s):
    return s[::-1]

s =str(input("Enter the string: "))  

reversed = reverse_string(s)

print(reversed)
