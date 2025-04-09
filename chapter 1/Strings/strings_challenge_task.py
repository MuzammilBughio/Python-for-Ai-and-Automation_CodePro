# Problem: Create a Python script that asks the user for their full name, removes any extra
# spaces, and then displays the following:
# ● The full name in uppercase.
# ● The full name in lowercase.
# ● The number of characters (excluding spaces).
# ● The first and last name separately.

full_name = input("Enter your full name: ").strip()

# Remove extra spaces
clean_name = " ".join(full_name.split())

# Convert to uppercase and lowercase
print("Uppercase:", clean_name.upper())
print("Lowercase:", clean_name.lower())

# Count characters excluding spaces
char_count = len(clean_name.replace(" ", ""))
print("Character Count (excluding spaces):", char_count)

# Extract first and last name
name_parts = clean_name.split()
if len(name_parts) >= 2:
    print("First Name:", name_parts[0])
    print("Last Name:", name_parts[-1])
else:
    print("First Name:", name_parts[0])
    print("Last Name: Not provided")
