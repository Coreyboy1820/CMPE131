def merge(list1, list2):
    new_list = []
    i = 0
    j = 0
    len_list1 = len(list1)
    len_list2 = len(list2)
    while i < len_list1 and j < len_list2:
        if list1[i] <= list2[j]:
            new_list.append(list1[i])
            i+=1
        elif list1[i] > list2[j]:
            new_list.append(list2[j])
            j+=1
    if i < len_list1:
        new_list.extend(list1[i:])
    elif j < len_list2:
        new_list.extend(list2[j:])
    return new_list
