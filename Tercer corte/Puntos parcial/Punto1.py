def interleave_strings(list1: list, list2: list) -> list:
    new_list = []
    for i in range(len(max(list1, list2))):
        if i < len(list1):
            new_list.append(list1[i])
        if i < len(list2):
            new_list.append(list2[i])
    return new_list


first = ["a", "b", "c", "d", "e"]
second = ["1", "2", "3"]
third = ["x"]

print(interleave_strings(first, second))