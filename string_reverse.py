# String Manipulation Program

text = input("Enter a string: ")

# Length
print("Length of string:", len(text))

# Uppercase
print("Uppercase:", text.upper())

# Lowercase
print("Lowercase:", text.lower())

# Reverse
print("Reversed string:", text[::-1])

# Palindrome Check
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")

# Vowel Count
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)

# Word Count
words = text.split()
print("Number of words:", len(words))

# Replace Spaces
print("After replacing spaces:", text.replace(" ", "_"))
