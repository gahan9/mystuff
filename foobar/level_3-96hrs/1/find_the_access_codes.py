def answer(l):
    sorted_list = sorted(l)
    print("-------------------------------------------")
    print(sorted_list)
    successor_dict = {}
    for x in sorted_list:
        if not successor_dict.__contains__(x):
            successor_dict[x] = set()
            for y in sorted_list[sorted_list.index(x)+1::]:
                if y%x==0:
                    if not successor_dict[x].__contains__(y):
                        successor_dict[x].add(y)

    # up_to now pair_count will be 0 only if no same number is in list more than twice
    # print(successor_dict)
    elements_evaluated = []
    final_elements=[]
    for elements in successor_dict:
        if elements not in elements_evaluated:
            elements_evaluated.append(elements)
            for sub_element in successor_dict[elements]:
                sub_element_length = len(successor_dict[sub_element])
                for sub_sub in successor_dict[sub_element]:
                    if elements == sub_element == sub_sub and sorted_list.count(sub_sub)<3:
                        continue
                    else:
                        final_elements.append((elements,sub_element,sub_sub))
    # print(final_elements)
    return len(set(final_elements))


from random import randint
# val_lis = [randint(40,500) for val in range(1000)]
# print(answer(val_lis))
print(answer([1,2,3,5,7,11,13,13, 26, 13, 13, 13, 26, 26]))
# print(answer([1, 1, 1, 2, 4]))
# print(answer([1, 1, 1]))
# print(answer([1, 3, 6, 6, 12, 12]))
# print(answer([97, 1, 3, 4, 12, 24]))
# print(answer([2, 3, 4, 5, 8, 12, 24, 40, 60]))
# print(answer([2, 3]))
# print(answer([2, 3, 4]))
