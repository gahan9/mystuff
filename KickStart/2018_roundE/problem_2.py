from sys import stdin

input = stdin.readline


def countSetBits( n ):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

class Problem(object):
    def __init__(self):
        pass


if __name__ == "__main__":
    t = int(input())
    for test in range(1, t+1):
        n, m, p = map(int, input().strip().split())
        ns = [int(input().strip(), 2) for i in range(1, n+1)]
        # print(">>", ns)
        ms = [int(input().strip(), 2) for i in range(1, m+1)]
        # complaints = 0
        complain_lis = []
        for i in range(int('1001001111', 2)):
        # for i in range(int('1'*p, 2)):
            if i not in ms:
                complaints = 0
                for j in ns:
                    compl = bin(i ^ j).count('1')
                    # print("select: {1:{0}b} \t demand: {2:{0}b} \t comp: {3}".format(p, i, j, compl))
                    # if i == 0 or j == 0:
                    #     compl -= 1
                    complaints += compl
                complain_lis.append(complaints)
        #         print("select: {1:{0}b} \t complaints: {2}".format(p, i, complaints))
        # print(complain_lis)
        ans = min(complain_lis) if complain_lis else 0
        print("Case #{}: {}".format(test, ans))
