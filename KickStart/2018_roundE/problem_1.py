from sys import stdin

input = stdin.readline


class Problem(object):
    def __init__(self):
        pass


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t+1):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        a.sort()
        count = 0
        for i in range(n):
            len_a = len(a)
            count = count+k if len_a > k else count + len_a
            a = a[k:]
            a = [x-1 for x in a if x-1 > 0]
        print("Case #{}: {}".format(test, count))
