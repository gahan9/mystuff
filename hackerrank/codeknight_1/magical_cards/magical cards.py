"""
Alice found a magical deck of cards numbered from 2 to 1,00,000. Alice will pick up a card and she has to tell the number of ways she can make that number printed on card by using their prime factors else she will die. She doesn’t know how to find this. Being Alice's friend you have to help her in finding out number of permutations.

Input Format

First line of the input consists of an integer T (no. of testcases).
Each testcase contains a single integer N.

Constraints

    1 <= T <= 100000
    1 < N <= 100000

Output Format

Print a single integer (number of ways she can make a number by their prime factors) for each testcase.

Sample Input 0

    3
    12
    6
    29

Sample Output 0

    3
    2
    1

Explanation 0

For first testcase, N=12; prime factors=2,2,3
No of ways:
1. 2*2*3
2. 2*3*2
3. 3*2*2
Hence, 3 ways are possible
"""

from functools import reduce
from collections import Counter


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def factorial(n):
    if n <= 1:
        return 1
    return reduce(lambda x, y: x * y, list(range(1, n + 1)))


def permutation(unique_numbers, total_number_count):
    numerator = factorial(total_number_count)
    denominator = 1
    for i in unique_numbers.values():
        denominator *= factorial(total_numbers-i)
    return numerator // denominator


total_numbers = int(input())

for _ in range(total_numbers):
    number = int(input())
    factors = prime_factors(number)
    number_count = Counter(factors)
    factor_len = len(factors)
    if factor_len == len(number_count):
        print(factorial(factor_len))
    else:
        print(permutation(number_count, factor_len))
