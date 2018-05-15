import math
# from collections import OrderedDict
#
#
# def euclidean_distance(coordinate1, coordinate2):
#     import math
#     return math.sqrt((coordinate1[0] - coordinate2[0]) ** 2 + (coordinate1[1] - coordinate2[1]) ** 2)
#
#
# def main():
#     coordinates_graph = OrderedDict()
#     total_trees, total_capacity = input().split()
#     total_trees, total_capacity = int(total_trees), float(total_capacity)
#     data_set = []
#     tree_coordinates = []
#     for _ in range(total_trees):
#         x, y, monkeys, capacity = map(int, input().split())
#         tree_coordinates.append((x, y))
#         data_set.append([(x, y), monkeys, capacity])
#         coordinates_graph[(x, y)] = [monkeys, capacity]
#
#     def find_path(graph, start, end, path=[]):
#         path = path + [start]
#         if start == end and euclidean_distance(start, end) <= total_capacity:
#             return path
#         for node in graph.keys():
#             if node not in path:
#                 prev_monkey, prev_threshold = graph[node]
#                 nxt_monkey, nxt_threshold = graph[node]
#                 if prev_monkey <= prev_threshold and nxt_monkey <= nxt_threshold:
#                     newpath = find_path(graph, node, end, path)
#                     if newpath:
#                         return newpath
#         return None
#
#     for i in coordinates_graph:
#         for j in coordinates_graph:
#             if not i == j:
#                 path_result = find_path(coordinates_graph, i, j)
#                 if path_result:
#                     if len(path_result) == total_trees:
#                         return ' '.join(map(lambda x: str(tree_coordinates.index(x)), path_result))
#     return -1
#
#
# print(main())


class FloodInJungle(object):
    def __init__(self, data):
        self.data = data
        self.data_size = len(self.data)

    @staticmethod
    def euclidean_distance(coordinate1, coordinate2):
        import math
        return math.sqrt((coordinate1[0] - coordinate2[0])**2 + (coordinate1[1] - coordinate2[1])**2)

    def get_paths(self):
        paths = []
        for i in range(self.data_size):
            # print(i, data_set[i])
            p = [i]
            for j in range(self.data_size):
                if i is not j:
                    # print(j, data_set[j])
                    # print(data_set[p[-1]], data_set[j], sep=" | ", end=" | ")
                    if self.euclidean_distance(self.data[p[-1]][0], self.data[j][0]) < total_capacity:
                        current_node_monkey, current_node_jump_threshold = self.data[p[-1]][1:]
                        nxt_node_monkey, nxt_node_jump_threshold = self.data[j][1:]
                        if current_node_monkey <= current_node_jump_threshold and nxt_node_monkey <= nxt_node_jump_threshold:
                            p.append(j)
                        elif current_node_monkey > current_node_jump_threshold and nxt_node_monkey <= nxt_node_jump_threshold:
                            self.data[j][-1] = 0
                            p.append(j)
                        elif current_node_monkey <= current_node_jump_threshold and nxt_node_monkey > nxt_node_jump_threshold:
                            self.data[p[-1]][-1] = 0
                            p.append(j)
                        # print(p)
                    else:  # saves a lot of time
                        # print(p)
                        break
            if len(p) == total_trees:
                paths.append(p)
        if paths:  # [[0, 1, 2], [1, 0, 2], [2, 0, 1]]
            return ' '.join(map(str, paths[0]))
        else:
            return -1


if __name__ == "__main__":
    # flag = "test"
    # # flag = "live"
    # if flag == "test":
    #     # test 1
    #     data_set = [[(1, 10), 5, 20], [(5, 10), 5, 20], [(8, 10), 5, 20]]
    #     # test 2
    #     # data_set = [[(1, 10), 5, 5], [(5, 10), 5, 1], [(8, 10), 5, 4]]
    #     total_trees, total_capacity = '3 100.0'.split()
    #     total_trees, total_capacity = int(total_trees), float(total_capacity)
    # else:
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
