"""
Project Euler #201: Subsets with a unique sum
https://www.hackerrank.com/contests/projecteuler/challenges/euler201/submissions/code/69127830
"""


def get_result(integers, subset_elements):
    import itertools
    sum_set = [sum(i) for i in itertools.combinations(integers, subset_elements)]
    x = []
    [x.append(i) for i in sum_set if sum_set.count(i) == 1]
    return sum(x)


if __name__ == '__main__':
    total_integers, subset_length = list(map(int, input().strip().split()))
    _integers = set(map(int, input().strip().split()))
    answer = get_result(_integers, subset_length)
    print(answer)
