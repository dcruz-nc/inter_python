def get_combined_dict(my_dict_1, my_dict_2):
    combined_dict = {}

    for i in my_dict_1.keys():
        if i in my_dict_2: # if they are matching
            combined_dict[i] = my_dict_1[i] + my_dict_2[i] #add to new dict

    return combined_dict


my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}

combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)