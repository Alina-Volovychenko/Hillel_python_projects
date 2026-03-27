# task1
import math
user_input = input("Please enter the integer number: ")
print(type(user_input))  # <class 'str'>
number = int(user_input)
print(number ** 2)

# task2
a = float(input("Enter 1st number: "))
b = float(input("Enter 2d number: "))
c = float(input("Enter 3d number: "))
average = (a + b + c) / 3
print("Average number:", average)

# task3
minutes = int(input("Enter minutes: "))
hours = minutes // 60
minutes = minutes % 60
print(hours, "часов и", minutes, "минут")

# task4
price = float(input("Enter price: "))
discount = float(input("Enter discount (%): "))
price_with_discount = price - (price * discount / 100)
print("Price with discount: ", price_with_discount)

# task5
number = int(input("Enter a number: "))
last_digit = number % 10
print("Last digit", last_digit)

# task6
length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter = 2 * (length + width)
print("Perimeter:", perimeter)

# task7
number = int(input("Enter a number consisting of four digits "))
first_number = number // 1000
second_number = (number // 100) % 10
third_number = (number // 10) % 10
fourth_number = number % 10
print(first_number)
print(second_number)
print(third_number)
print(fourth_number)