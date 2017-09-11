def answer(l):
    successor_dict = {}
    pair_count = 0
    for x in range(len(l)):
        a = l[x]
        successor_dict[x] = []
        for y in range(x + 1, len(l)):
            b = l[y]
            if (b % a) == 0:
                successor_dict[x].append(y)
    # print(successor_dict)

    for element in successor_dict:
        for sub_element in successor_dict[element]:
            for sub_sub in successor_dict[sub_element]:
                print(element, sub_element, sub_sub)
            pair_count += len(successor_dict[sub_element])

    return pair_count


print(answer([val for val in range(1, 1000) if val % 2 == 0] + [1, 1, 1, 2, 2, 2]))
print(answer([1, 2, 3, 4, 5, 6]))
print(answer([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]))
print(answer([1, 1, 1, 2, 4]))
print(answer([1, 3, 6, 6, 12, 12]))
print(answer([97, 1, 3, 4, 12, 24]))
print(answer([2, 3, 4, 5, 8, 12, 24, 40, 60]))
print(answer([2, 3]))
print(answer([2, 3, 4]))
