# Create a function that generates a random number between a given range.
import random


def generate_random_number(start_range, stop_range):
    if start_range < stop_range:
        print(random.randint(start_range, stop_range))
    else:
        print("The start number must be less than the stop number.")


generate_random_number(5, 10)
