def sort_dictionary(my_dict):
    new_list = []
    while len(my_dict) != 0:
        smallest_phone_number = 0
        smallest_name = ""
        for i, (key, value) in enumerate(my_dict.items()):
            if i == 0:
                smallest_tuple = value
                smallest_name = key
            else:
                if value[1] < smallest_tuple[1]:
                    smallest_name = key
                    smallest_tuple = value
        new_list.append((smallest_name, smallest_tuple[0]))
        del my_dict[smallest_name]
    return new_list
