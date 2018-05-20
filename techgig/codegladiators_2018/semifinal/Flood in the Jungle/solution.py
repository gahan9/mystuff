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
        self.euclidean_dict = self.construct_dict()
        self.meetup_tree = []

    @staticmethod
    def euclidean_distance(coordinate1, coordinate2):
        return math.sqrt((coordinate1[0] - coordinate2[0])**2 + (coordinate1[1] - coordinate2[1])**2)

    def construct_dict(self):
        d = {}
        for i in self.data.keys():
            for j in self.data.keys():
                if i is not j:
                    if self.euclidean_distance(i, j) <= self.threshold:
                        d[i] = d.get(i, []) + [j] + d.get(j, [])
        return d

    def get_paths(self):
        if len(self.non_capable_tree) == 1:
            end_tree = self.non_capable_tree[0]
            idx = self.data[end_tree][2]
            reach1 = list(self.data.keys())[:idx]
            reach2 = list(self.data.keys())[idx+1:]
            reach3 = reach1 + reach2
            if self.sub_calc(reach3, [end_tree]):
                return idx
            elif self.sub_calc(reach1, [end_tree]) and self.sub_calc(reach2, [end_tree]):
                return idx
            else:
                return -1
        for path in self.permutations:
            # print(path, '|', list(map(lambda x: self.data[x], path)))
            p = []
            for nxt in path:  # path[i] = ((1, 10), (5, 10), (8, 10))
                # nxt = path[i]
                monkey_sum = 0
                try:
                    prev = p[-1]
                    if self.euclidean_distance(prev, nxt) <= self.threshold:
                        prev_monkey, prev_limit, prev_idx, capability_ = self.data[prev]
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
        return self.calculate()

    def sub_calc(self, dataset, elem):
        size = len(dataset)
        flag = True
        for i in self.data.keys():
            if self.euclidean_distance(i, elem[0]) > self.threshold:
                flag = False
        if flag:
            return flag
        for i in permutations(dataset, size):
            path = list(i) + elem
            print(path)
            p = []
            monkey_sum = 0
            for nxt in path:
                try:
                    prev = p[-1]
                    if self.euclidean_distance(prev, nxt) > self.threshold:
                        break
                    else:
                        prev_monkey, prev_limit, prev_idx, capability = self.data[prev]
                        monkey_sum += prev_monkey
                        if monkey_sum > prev_limit:
                            break
                        else:
                            p.append(nxt)
                except IndexError:
                    p.append(nxt)
            print(p, size)
            if len(p) is size + 1:
                return True
        return False

    def find_all_paths(self, graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []  # maintain a list to store all explored path
        for node in graph[start]:
            if node not in path:
                new_paths = self.find_all_paths(graph, node, end, path)
                for new_path in new_paths:
                    if len(new_path) is self.data_size:
                        # print(">>>", new_path[-1], self.data[new_path[-1]][2])
                        self.meetup_tree.append(self.data[new_path[-1]][2])
                        paths.append(new_path)  # add new path to list instead of returning it.
        return paths

    def calculate(self):
        if len(self.non_capable_tree) == 1:
            end_tree = self.non_capable_tree[0]
            idx = self.data[end_tree][2]
            reach1 = list(self.data.keys())[:idx]
            reach2 = list(self.data.keys())[idx+1:]
            reach3 = reach1 + reach2
            if self.sub_calc(reach3, [end_tree]):
                return idx
            elif self.sub_calc(reach1, [end_tree]) and self.sub_calc(reach2, [end_tree]):
                return idx
            else:
                return -1
        else:
            for i in self.data.keys():
                for j in self.data.keys():
                    if i is not j:
                        _paths = self.find_all_paths(self.euclidean_dict, i, j)
                        if _paths:
                            pass
            if self.meetup_tree:
                return ' '.join(map(str, sorted(set(self.meetup_tree))))
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
    if len(non_capable_trees) > 1:
        print("-1")
    else:
        print(f.get_paths())


"""
3 100.0
1 10 5 5
5 10 5 1
8 10 5 4

-1


3 100.0
1 10 5 20
5 10 5 20
8 10 5 20

0 1 2


4 2.0
1 10 5 5
3 10 5 5
5 10 7 5
7 10 5 20

-1


5 10.0
1 10 5 5  		
2 10 15 15
5 10 5 1
8 10 0 0
15 10 0 0

-1


4 2.0
1 10 5 20
3 10 5 20
5 10 5 20
7 10 5 20

0 1 2 3


3 100.0
1 10 5 5
-50 -10 0 6
-40 -50 0 5

0 1 2


4 2.0
1 10 5 5
3 10 5 10
5 10 7 5
7 10 5 20
"""