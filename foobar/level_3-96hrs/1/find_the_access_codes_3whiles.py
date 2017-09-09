def counter(myList) :
    x = len(myList)
    if (x < 3) :
        return 0
    count1 = 0
    count2 = 0
    count3 = 0
    answer = 0
    final = []
    while(count1 < x-2) :
        count2 = count1 + 1
        while(count2 < x-1) :
            y = myList[count2] % myList[count1]
            if (y == 0) :
                count3 = count2 + 1
                while (count3 < x):
                    y = myList[count3] % myList[count2]
                    if (y == 0) :
                        final.append(str(myList[count1]) + str(myList[count2]) + str(myList[count3]))
                    count3 += 1
            count2 += 1
        count1 += 1
    return len(set(final))

print(counter([1, 2, 3, 4, 5, 6]))
print(counter([1, 1, 1]))
print(counter([1, 3, 6, 12, 12]))
print(counter([97, 1, 3, 4, 12, 24]))
print(counter([2, 3, 4, 5, 8, 12, 24, 40, 60]))
print(counter([2, 3]))
print(counter([2, 3, 4]))