import math
from collections import OrderedDict
from itertools import permutations


class FloodInJungle(object):
    def __init__(self, data, threshold, non_capable_tree):
        self.data = data
        self.threshold = threshold
        self.data_size = len(self.data)
        self.permutations = permutations(self.data.keys(), self.data_size)
        self.non_capable_tree = non_capable_tree

    @staticmethod
    def euclidean_distance(coordinate1, coordinate2):
        return math.sqrt((coordinate1[0] - coordinate2[0])**2 + (coordinate1[1] - coordinate2[1])**2)

    def get_paths(self, data, size, **kwargs):
        value = kwargs.get('elem', None)
        for i in permutations(data, size):  # print(path, '|', list(map(lambda x: self.data[x], path)))
            if value:
                path = list(i) + value
            else:
                path = i
            p = []
            for nxt in path:  # path[i] = ((1, 10), (5, 10), (8, 10))
                try:
                    prev = p[-1]
                    if self.euclidean_distance(prev, nxt) <= self.threshold:
                        prev_monkey, prev_limit, prev_idx, capability = self.data[prev]
                        if prev_monkey <= prev_limit:  # print(">>> ", prev, nxt, self.euclidean_distance(prev, nxt), p)
                            p.append(nxt)
                    else:
                        break
                except IndexError:
                    p.append(nxt)
            # print("--* ", p, size)
            checker = size + 1 if value else size
            if len(p) is checker:
                return p
        # if paths:  # [[0, 1, 2], [1, 0, 2], [2, 0, 1]]
        #     return ' '.join(map(str, [self.data[i][2] for i in paths[0]]))
        return 0

    def get_results(self):
        if len(self.non_capable_tree) == 1:
            end_tree = self.non_capable_tree[0]
            reach1 = list(self.data.keys())[:self.data[end_tree][2]]
            reach2 = list(self.data.keys())[self.data[end_tree][2]+1:]
            reach3 = reach1 + reach2
            # print(reach1, reach2, reach3, sep="\n>>")
            r1_path = self.get_paths(reach1, len(reach1), elem=[end_tree])
            r2_path = self.get_paths(reach2, len(reach2), elem=[end_tree])
            r3_path = self.get_paths(reach3, len(reach3), elem=[end_tree])
            # print(r1_path, r2_path, r3_path)
            if (r1_path and r2_path) or r3_path:
                return self.data[end_tree][2]
            else:
                return -1
        elif len(self.non_capable_tree) < 1:
            paths = self.get_paths(self.data.keys(), self.data_size)
            return ' '.join(map(str, [self.data[i][2] for i in paths]))
        else:
            return -1


if __name__ == "__main__":
    total_trees, total_capacity = input().split()
    total_trees, total_capacity = int(total_trees), float(total_capacity)
    coordinates = OrderedDict()
    index = 0
    non_capable_trees = []
    for _ in range(total_trees):
        x, y, monkeys, capacity = map(int, input().split())
        capability = 1 if monkeys <= capacity else 0
        coordinates[(x, y)] = [monkeys, capacity, index, capability]
        if not capability:
            non_capable_trees.append((x, y))
        index += 1
    f = FloodInJungle(coordinates, total_capacity, non_capable_trees)
    print(f.get_results())


"""
3 100.0
1 10 5 20
5 10 5 20
8 10 5 20

4 2.0
1 10 5 5
3 10 5 5
5 10 7 5
7 10 5 20

5 10.0
1 10 5 5  		
2 10 15 15
5 10 5 1
8 10 0 0
15 10 0 0
"""