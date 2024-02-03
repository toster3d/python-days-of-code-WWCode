# Write a program to check if a number is positive, negative, or zero.

def check_if_positive(number):
    if number == 0:
        print("The number is 0.")
    elif number % 2 == 0:
        print(f"The numer {number} is positive.")
    else:
        print(f"The number {number} is negative.")


check_if_positive(123)
