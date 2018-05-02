class Graph(object):
    def __init__(self, *args, **kwargs):
        self.explored_path = {}

    def find_path(self, graph, start, end, path=[]):
        """
        simple function to determine a path between two nodes
        algorithm paradigm: backtracking
        :param start: start node
        :param end: end node
        :param path: explored path between start and end nodes
                    This argument is used to avoid cycles
        :return:a list of nodes (including the start and end nodes) comprising the path.
                When no path can be found, it returns None
        """
        if self.path_exist((start, end)):
            return self.explored_path[(start, end)]
        path = path + [start]  # creates a new list.
        # If we had written "path.append(start)" instead,
        # we would have modified the variable 'path' in the caller
        if start == end:
            return path  # start and end node are same
        for node in graph[start]:  # explore nodes in corresponding start node
            if node not in path:  # If current node is unexplored then proceed ahead
                if (node, end) in self.explored_path:
                    # print("HIT", node, end)
                    new_path = self.explored_path[(node, end)]
                else:
                    # print("Miss", start, end)
                    new_path = self.find_path(graph, node, end, path)  # find path from current node(as start node) to end node
                if new_path:
                    self.explored_path[(start, end)] = new_path[len(path)-1:]
                    # print("returning...", start, end, path, new_path[len(path)-1:])
                    return new_path  # if new_path found between nodes then return the new_path
        # self.explored_path[(start, end)] = path
        return None  # no path can be found, returns None

    def path_exist(self, _tuple):
        return bool(_tuple in self.explored_path)


def main():
    graph_obj = Graph()  # Graph object
    # construct a basic graph
    nodes, visit_days = map(int, input().split())
    adj_list = {}
    for _ in range(1, nodes):
        u, v = map(int, input().split())
        adj_list.setdefault(u, []).append(v)
        adj_list.setdefault(v, []).append(u)
    # print(adj_list)
    gift_count = {}
    for _ in range(visit_days):
        start_home, end_home = map(int, input().split())
        _path = graph_obj.find_path(adj_list, start_home, end_home)
        # print(graph_obj.explored_path, _path)
        for i in _path:
            gift_count[i] = gift_count.setdefault(i, 0) + 1
    print(max(gift_count.values()))


if __name__ == "__main__":
    main()
