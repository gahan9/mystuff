import math
import pdb


class FloodInJungle(object):
    def __init__(self, data):
        self.data = data
        self.data_size = len(self.data)

    @staticmethod
    def euclidean_distance(coordinate1, coordinate2):
        return math.sqrt((coordinate1[0] - coordinate2[0])**2 + (coordinate1[1] - coordinate2[1])**2)

    def get_paths(self):
        paths = []
        for i in range(self.data_size):
            # print(i, data_set[i])
            p = [i]
            for j in range(self.data_size):
                if not i == j:
                    # print(j, data_set[j])
                    # print(euclidean_distance(data_set[i][0], data_set[j][0]))
                    if self.euclidean_distance(self.data[i][0], self.data[j][0]) < total_capacity:
                        current_node_monkey, current_node_jump_threshold = self.data[i][1:]
                        nxt_node_monkey, nxt_node_jump_threshold = self.data[j][1:]
                        if current_node_monkey <= current_node_jump_threshold and nxt_node_monkey <= nxt_node_jump_threshold:
                            p.append(j)
            if len(p) == total_trees:
                paths.append(p)
        if paths:  # [[0, 1, 2], [1, 0, 2], [2, 0, 1]]
            return ' '.join(map(str, paths[0]))
        else:
            return -1


if __name__ == "__main__":
    # flag = "test"
    flag = "live"
    if flag == "test":
        coordinates = {(1, 10): [5, 20], (5, 10): [5, 20], (8, 10): [5, 20]}
        # test 1
        data_set = [[(1, 10), 5, 20], [(5, 10), 5, 20], [(8, 10), 5, 20]]
        # test 2
        # data_set = [[(1, 10), 5, 5], [(5, 10), 5, 1], [(8, 10), 5, 4]]
        total_trees, total_capacity = '3 100.0'.split()
        total_trees, total_capacity = int(total_trees), float(total_capacity)
    else:
        total_trees, total_capacity = input().split()
        total_trees, total_capacity = int(total_trees), float(total_capacity)
        coordinates = {}
        data_set = []
        for _ in range(total_trees):
            x, y, monkeys, capacity = map(int, input().split())
            data_set.append([(x, y), monkeys, capacity])
            coordinates[(x, y)] = [monkeys, capacity]
    f = FloodInJungle(data_set)
    print(f.get_paths())
