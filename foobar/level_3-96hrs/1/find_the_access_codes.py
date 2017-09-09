def answer(l):
    # print("-------------------------------------------")
    sorted_list = sorted(l)
    # print(sorted_list)
    # check_div = lambda num1, num2 : num2%num1==0
    successor_dict = {}
    pair_count = 0

    # get successors of all elements at end of the for loop (worst case : 185ms, best case : <1ms (minimum in micro seconds))
    for x in sorted_list:
        # if sorted_list.count(x) >=3 and x not in successor_dict.keys():
        #     pair_count += 1
        if x not in successor_dict.keys():
            successor_dict[x] = []
            for y in sorted_list[sorted_list.index(x)+1::]:
                if y%x==0:
                    if y not in successor_dict[x]:
                        successor_dict[x].append(y)
                    for z in sorted_list[sorted_list.index(y)+1::]:
                        if z%y==0:
                            if z not in successor_dict[x]:
                                successor_dict[x].append(z)
                        if z%x==0:
                            if z not in successor_dict[x]: 
                                successor_dict[x].append(z)
        else:
            pass
    final_successor_dict= {i:sorted(successor_dict[i]) for i in successor_dict}
    # print("unsorted element: {0} \nsorted element: {1} ".format(successor_dict, final_successor_dict))

    # up_to now pair_count will be 0 only if no same number is in list more than twice
    elements_evaluated = []
    for elements in successor_dict:
        if elements not in elements_evaluated:
            elements_evaluated.append(elements)
            for sub_element in successor_dict[elements]:
                if sub_element not in elements_evaluated:
                    elements_evaluated.append(sub_element)
                    sub_element_length = len(successor_dict[sub_element])
                    if not sub_element_length == 0:
                        pair_count += sub_element_length


    return pair_count


from random import randint
val_lis = [randint(1,555555) for val in range(2000)]
print(answer(val_lis))
print(answer([1, 2, 3, 4, 5, 6]))
print(answer([1, 1, 1]))
print(answer([1, 3, 6, 12, 12]))
print(answer([97, 1, 3, 4, 12, 24]))
print(answer([2, 3, 4, 5, 8, 12, 24, 40, 60]))
print(answer([2, 3]))
print(answer([2, 3, 4]))

