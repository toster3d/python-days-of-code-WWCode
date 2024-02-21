# Write a program that uses recursion to generate all permutations of a list

list=["A", "B", "C", "D"]

def check_permutation(list_length):
    if list_length == 0 or list_length == 1:
        return 1
    else:
        return list_length * check_permutation(list_length - 1)

    
print(check_permutation(len(list)))  # Output: 24
