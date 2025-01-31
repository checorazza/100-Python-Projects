text = "Hello world! This is a text to test string methods."

# Capitalize the first letter of the string
print(text.capitalize())

# Convert the string to uppercase
print(text.upper())

# Convert the string to lowercase
print(text.lower())

# Swap the case of the string
print(text.swapcase())

# Get the length of the string
print(len(text))

# Count the number of times a substring appears in the string
print(text.count("is"))

# Find the index of the first occurrence of a substring
print(text.find("is"))

# Check if the string starts with a substring
print(text.startswith("Hello"))

# Check if the string ends with a substring
print(text.endswith("methods."))

# Replace a substring with another substring
print(text.replace("world", "Python"))

# Split the string into a list of substrings
print(text.split())

# Slice the string
print(text[6:11])

# Multiply the string
print(text * 3)

# Remove leading and trailing whitespaces
text = "    Hello world!    "
print(text.strip())

