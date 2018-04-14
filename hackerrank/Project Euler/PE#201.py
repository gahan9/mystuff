"""
Project Euler #201: Subsets with a unique sum
https://www.hackerrank.com/contests/projecteuler/challenges/euler201/submissions/code/69127830
"""
import itertools


def get_result(integers, subset_length):
    print(integers, subset_length)
    sum_set = [i for i in itertools.combinations(integers, subset_length)]
    print(sum_set)
    _unique = []
    _duplicates = []
    for i in sum_set:
        if i not in _unique:
            _sum = sum(i)
            if _sum not in _unique and _sum not in _duplicates:
                _unique.append(_sum)
            else:
                _unique.pop(_unique.index(_sum))
                _duplicates.append(_sum)
    return sum(_unique)


if __name__ == '__main__':
    total_integers, subset_length = list(map(int, '100 25'.strip().split()))
    # _integers = list(map(int, input().strip().split()))
    # _integers = range(500, 10500, 100)
    _integers = range(500, 10500, 100)
    answer = get_result(_integers, subset_length)
    print(answer)
