filename = input("Enter filename: ")

try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: file not found")
    exit()

words = content.split()
word_counter = len(words)
print("The total number of words in the file is",word_counter)