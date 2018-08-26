from itertools import combinations, combinations_with_replacement
from sys import stdin

from more_itertools import distinct_permutations

input = stdin.readline


class Problem(object):
    def __init__(self):
        pass


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t+1):
        n = int(input())
        bahu = list(map(int, input().split()))
        bala = list(map(int, input().split()))
        # bahu_battlefield = [bahu[i:i + n] for i in range(0, len(bahu), n)]
        bala_battlefield = [bala[i:i + n] for i in range(0, len(bala), n)]
        count = 0
        victory_lis = []
        for bahu_lis in set(distinct_permutations(bahu)):
            i_battlefield = [bahu_lis[i:i + n] for i in range(0, len(bahu_lis), n)]
            win_count = 0
            for i in range(n):
                count += 1
                if sum(i_battlefield[i]) > sum(bala_battlefield[i]):
                    win_count += 1
            victory_lis.append(win_count)
        ans = "1.000000000" if max(victory_lis) > (n/2) else win_count/count
        print("Case #{}: {}".format(test, ans))
