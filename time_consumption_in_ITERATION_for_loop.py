import time
ls = ['element1', 'element2', 'element3', 'element4', 'element5', 'element6', 'element7', 'element8', 'element9', 'element10']
ls = ls*10000

start1 = time.clock()
#m1. Step for loop by size two with if condition 
for x in ls:
    if ls.index(x)%2 == 0:
        # my code to be process
        print(end='') # for simplicity I just printed element
print()
print(time.clock() - start1)



start2 = time.clock()
#m2. tried another way like below:
for x in range(0, len(ls), 2):
    # this way give me output of alternate element from list
    print(end='')
print()
print(time.clock() - start2)

start3 = time.clock()
import itertools
for item in itertools.islice(ls, None, None, 2):  # start and stop None, step 2
    print(end='')
print()
print(time.clock() - start3)



start4 = time.clock()
for x in ls[::2]:
    print(end='')
print()
print(time.clock() - start4)