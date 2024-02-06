Create a program to find the second-largest element in a list.

def find_second_largest(elements):
    highest_no = max(elements)
    elements.remove(highest_no)
    return max(elements)


given_list = [-1, -7, 3, -4, -5]
print(f"The second largest element in the list is {find_second_largest(given_list)}.")   #Outpot: The second largest element in the list is -1.
