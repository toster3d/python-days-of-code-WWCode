vowels = ['a', 'e', 'i', 'o', 'u', 'y']


def count_vowels(word):
    counter = 0
    for letter in word:
        if letter in vowels:
            counter += 1
    return counter


given_word = input("Write a word: ").lower()

number_of_vowels = count_vowels(word)
print(f"Number of vowels in {given_word.title()} is: {number_of_vowels}")
