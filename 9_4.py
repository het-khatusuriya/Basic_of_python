# Open the file
file = open("example.txt", "r")

# Read the text from the file and split it into words
words = file.read().split()

# Print the first 5 words
print(words[:5])

# Close the file
file.close()
