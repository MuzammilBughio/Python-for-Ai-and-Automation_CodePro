#Extract the domain name from an email address (e.g., input: "user@example.com",(output: "example.com").

email = input("Enter an email address: ")
domain = email.split('@')[-1]
print("Domain:", domain)
