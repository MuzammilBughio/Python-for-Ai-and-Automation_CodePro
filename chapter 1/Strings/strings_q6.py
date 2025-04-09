#Write a Python script to extract the first and last word from a sentence entered by the user.

sentence = input("Enter a sentence: ")
words = sentence.split()
if words:
    print("First word:", words[0])
    print("Last word:", words[-1])
else:
    print("No words entered.")
