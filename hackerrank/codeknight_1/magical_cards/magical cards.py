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
from itertools import permutations


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
    return reduce(lambda x, y: x * y, [1] + list(range(1, n + 1)))


def permutation(n):
    return factorial(n) // factorial(n-1)


total_numbers = int(input())

for number in range(total_numbers):
    print(len(set(permutations(prime_factors(int(input()))))))
