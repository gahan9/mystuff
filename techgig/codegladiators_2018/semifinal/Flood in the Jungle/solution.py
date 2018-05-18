import math
from collections import defaultdict
from itertools import permutations


class FloodInJungle(object):
    def __init__(self, data, threshold):
        self.data = data
        self.threshold = threshold
        self.data_size = len(self.data)
        self.permutations = permutations(self.data.keys(), self.data_size)

    @staticmethod
    def euclidean_distance(coordinate1, coordinate2):
        return math.sqrt((coordinate1[0] - coordinate2[0])**2 + (coordinate1[1] - coordinate2[1])**2)

    def get_paths(self):
        for path in self.permutations:
            # print(path, '|', list(map(lambda x: self.data[x], path)))
            p = []
            for nxt in path:  # path[i] = ((1, 10), (5, 10), (8, 10))
                # nxt = path[i]
                monkey_sum = 0
                try:
                    prev = p[-1]
                    if self.euclidean_distance(prev, nxt) <= self.threshold:
                        prev_monkey, prev_limit, prev_idx = self.data[prev]
                        monkey_sum += prev_monkey
                        # nxt_monkey, nxt_limit, nxt_idx = data_set[nxt]
                        if monkey_sum <= prev_limit:
                            # print(">>> ", prev, nxt, self.euclidean_distance(prev, nxt), p)
                            p.append(nxt)
                    else:
                        break
                except IndexError:
                    p.append(nxt)
            # print(p)
            # print(len(p))
            if len(p) is self.data_size:
                return ' '.join(map(str, [self.data[i][2] for i in p]))
                # paths.append(p)
        return -1


if __name__ == "__main__":
    total_trees, total_capacity = input().split()
    total_trees, total_capacity = int(total_trees), float(total_capacity)
    coordinates = defaultdict()
    index = 0
    for _ in range(total_trees):
        x, y, monkeys, capacity = map(int, input().split())
        coordinates[(x, y)] = [monkeys, capacity, index]
        index += 1
    f = FloodInJungle(coordinates, total_capacity)
    print(f.get_paths())


"""
3 100.0
1 10 5 20
5 10 5 20
8 10 5 20
"""