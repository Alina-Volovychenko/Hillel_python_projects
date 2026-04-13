import string

text = input("Enter two letters separated by a hyphen: ")

start, end = text.split("-")

letters = string.ascii_letters

result = letters[letters.index(start):letters.index(end) + 1]

print(result)