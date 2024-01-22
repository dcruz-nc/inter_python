def unique_elements_list(input_list): # create unique elements list from input list
    unique_list = []
    for i in input_list: # i = element
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

test_list = [1, 2, 3, 1, 2, 4]
result = unique_elements_list(test_list)

print("Original list:", test_list)
print("New unique element list:", result)
