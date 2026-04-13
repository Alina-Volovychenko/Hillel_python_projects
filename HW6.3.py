number = input("Enter number: ")

while len(number) > 1:
    product = 1

    for digit in number:
        product *= int(digit)

    number = str(product)

print(number)