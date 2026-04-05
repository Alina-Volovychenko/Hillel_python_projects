import string
import keyword

name = input()

is_valid = True

if name[0].isdigit():
    is_valid = False

elif any(c.isupper() for c in name):
    is_valid = False

elif " " in name:
    is_valid = False

elif any(c in string.punctuation.replace("_", "") for c in name):
    is_valid = False

elif "__" in name:
    is_valid = False

elif name in keyword.kwlist:
    is_valid = False

print(is_valid)