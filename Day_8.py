# Write a function that accepts a string and calculates the number of uppercase and lowercase letters in it.

def count_upper_and_lower(word):
    uppers = 0
    lowers = 0
    for char in word:
        if char.isupper():
            uppers += 1
        elif char.islower():
            lowers += 1
    print(f"In the word: {word} is {uppers} upper letters and {lowers} lower letters.")


count_upper_and_lower("AnAcoNda")
