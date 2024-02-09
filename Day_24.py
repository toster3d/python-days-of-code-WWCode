# Write a program to remove vowels from a given string.

def remove_vowels(given_string):
    vowels = 'aeiouyAEIOUY'
    without_vowels = ''
    for char in given_string:
        if char not in vowels:
            without_vowels += char
    return without_vowels


string_without_vowels = remove_vowels("I Love Python.")
print(string_without_vowels)     # Output:  Lv Pthn.
