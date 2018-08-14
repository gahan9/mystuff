"""
Shubham and Subarrays
https://www.hackerrank.com/contests/codeknight-1/challenges/shubham-and-subarrays

Shubham wants to gift a present to his friend on her birthday. He visits n shops in sequential manner and looks for an item. Each item has a code written on it (an integer xi) Now, he is superstitious, he thinks that he can buy only from shops that are adjacent to each other and the product of the code written on their item is equal to k. So, he can only buy a present if there is a continuous segment (of length greater than or equal to 1) in the shops visited in which the product of codes is equal to k. You have to find the number of ways he can buy present for his friend.

Input Format

First line contains the number of testcases t. First line of each testcase contains two integers n (size of the array) and k (subarray product). Second line of each testcase contains n integers.

Constraints

    1 <= t <= 100
    1 <= n <= 10^5
    1 <= k <= 10^9
    1 <= xi <= 10^9

Output Format

In each line print the number of subarrays possible.

Sample Input 0

    1
    7 6
    2 3 3 2 3 2 6

Sample Output 0

    5

Explanation 0

The possibilties are in start and end index pairs [{0,1},{2,3},{3,4},{4,5},{6,6}]
"""