# Write a function is_even(n) that returns True if n is even and False otherwise.

def is_even(n):
    if((n %2)==0):
       return "True"
    else:
       return "False"
    

n = int(input("Enter the number: "))

answer = is_even(n)
print(answer)