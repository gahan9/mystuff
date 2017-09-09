def generate_prime_numbers(n):
    prime = [True for i in range(n+1)]
    p=2
    while(p*p <= n):
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
            # Update all multiples of p
            for i in range(p*2, n+1, p):
                prime[i] = False
        p+=1
    lis =[]
    # Print all prime numbers
    for p in range(2, n):
        if prime[p]:
            lis.append(p)
    return lis


def answer(l):
    print("-------------------------------------------")
    sorted_list = sorted(l, reverse=True)
    total_numbers = len(sorted_list)
        
    prime_numbers = generate_prime_numbers(sorted_list[0])
    check_div = lambda num1, num2 : num2%num1==0
    isPrime = lambda num : num in prime_numbers

    pairs=[]
    pair_count = 0
    ones_occurance = sorted_list.count(1)
    # print(sorted_list)
    for z in range(total_numbers-2):
        # tup=()
        cur_z = sorted_list[z]
        if isPrime(cur_z) and ones_occurance <=1:
            continue
        else:
            list2=sorted_list[0:z] + sorted_list[z+1::]
            # print(sorted_list, list2)
            for y in range(len(list2)-1):
                cur_y = list2[y]
                if isPrime(cur_y) and 1 not in l:
                    continue
                # elif cur_y == list2[y-1]:
                #     continue
                first_div = check_div(cur_y, cur_z)
                if not first_div and (cur_z==total_numbers-3 or cur_y==len(list2)-2):
                    return 0
                elif first_div:
                    # tup = (cur_y, cur_z)
                    list3=list2[0:y] + list2[y+1::]
                    # print(list3)
                    for x in range(len(list3)):
                        cur_x = list3[x]
                        if check_div(cur_x, cur_y):
                            tup = (cur_x, cur_y, cur_z)
                            if tup not in pairs:
                                pair_count +=1
                                pairs.append(tup)
    # print(pairs)
    return pair_count



from random import randint
val_lis = [randint(1,15000) for val in range(randint(1,1500))]
print(answer([1, 2, 3, 4, 5, 6]))
print(answer([1, 1, 1]))
print(answer([1, 3, 6, 12, 12]))
print(answer([1, 3, 6, 12, 12]))
print(answer([97, 1, 3, 4]))
print(answer([2,3,4,5,8,12,24,40,60]))
# print(answer(val_lis))
