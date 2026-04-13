import string

text = input("Enter text: ")

for ch in string.punctuation:
    text = text.replace(ch, "")

words = text.split()

hashtag = "#" + "".join(word.capitalize() for word in words)

hashtag = hashtag[:140]

print(hashtag)