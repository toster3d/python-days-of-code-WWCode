# Write a program that checks if a key exists in a dictionary.

dictionary = {
    'apple': 'fruit',
    'orange': "fruit",
    'potato': "vegetable",
    'carrot': 'vegetable'
}


def check_if_key_exists(key):
    if key in dictionary.keys():
        print(f'The key: {key} exists in a dictionary.')
    else:
        print(f"The key: {key} doesn't exists in a dictionary.")


check_if_key_exists('carrot')
