# Write a program to count the occurrences of a specific character in a string.

def sign_count(word, sign):
    return word.count(sign)


number_of_sign = sign_count("anaconda", "a")
print(number_of_sign)       # Output: 3
