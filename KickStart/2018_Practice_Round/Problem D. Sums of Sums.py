"""
Problem D. Sums of Sums

Alice presented her friend Bob with an array of N positive integers, indexed from 1 to N. She challenged Bob with many queries of the form "what is the sum of the numbers between these two indexes?" But Bob was able to solve the problem too easily.

Alice took her array and found all N*(N+1)/2 non-empty subarrays of it. She found the sum of each subarray, and then sorted those values (in nondecreasing order) to create a new array, indexed from 1 to N*(N+1)/2. For example, for an initial array [2, 3, 2], Alice would generate the subarrays [2], [3], [2], [2, 3], [3, 2], and [2, 3, 2] (note that [2, 2], for example, is NOT a subarray). Then she'd take the sums -- 2, 3, 2, 5, 5, 7 -- and sort them to get a new array of [2, 2, 3, 5, 5, 7].

Alice has given the initial array to Bob, along with Q queries of the form "what is the sum of the numbers from index Li to Ri, inclusive, in the new array?" Now Bob's in trouble! Can you help him out?
"""
from itertools import combinations


class SumsOfSums(object):
    def __init__(self, *args):
        self.element_list = args[0]
        self.sum_list = args[0]

    def get_sum_list(self):
        return self.sum_list

    def get_result(self, start_index, end_index, sums_list=None):
        if not sums_list:
            sums_list = self.sum_list
        return sum(sums_list[start_index - 1: end_index])

    def get_sub_array_sum(self, lis, lis_size):
        if not lis:
            lis = self.element_list
            lis_size = len(lis)
        final_list = []
        for i in range(lis_size):
            for j in range(1, lis_size+1):
                if i < j:
                    final_list.append(sum(lis[i:j]))
        return sorted(final_list)


if __name__ == "__main__":
    t = int(input())  # total test cases
    for p in range(1, t + 1):
        try:
            total_elements, queries = [int(s) for s in input().strip().split(" ")]
        except Exception as e:
            total_elements, queries = [int(s) for s in input().strip().split(" ")]
        initial_elements = [int(s) for s in input().strip().split(" ")]
        sum_obj = SumsOfSums(initial_elements)
        print("Case #{}:".format(p))
        target_lis = sum_obj.get_sub_array_sum(initial_elements, total_elements)
        for q in range(1, queries + 1):
            start, end = [int(s) for s in input().strip().split(" ")]
            print(sum_obj.get_result(start, end, target_lis))
