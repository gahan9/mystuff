class Graph(object):
    def __init__(self, graph_dict=None, *args, **kwargs):
        # This(self.default_graph) is a dictionary whose keys are the nodes of the graph.
        # For each key, the corresponding value is a list containing the nodes
        # that are connected by a direct arc from this node
        if graph_dict:
            self.__default_graph = graph_dict
        else:
            # initializes a graph object  If no dictionary or None is given
            self.__default_graph = {'A': ['B', 'C'],
                                    'B': ['C', 'D'],
                                    'C': ['D'],
                                    'D': ['C'],
                                    'E': ['F'],
                                    'F': ['C']}

    def find_shortest_path(self, graph, start, end, path=[]):
        """
        find shortest path from one node to other in given graph
        :param graph: graph structure
        :param start: start node
        :param end: end node
        :param path: explored path between start and end nodes
        :return: shortest path between two nodes
        """

        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None  # maintain a variable to check with every new explored path, replace existing with shortest one
        for node in graph[start]:
            if node not in path:
                new_path = self.find_shortest_path(graph, node, end, path)
                if new_path:
                    if not shortest or len(new_path) < len(shortest):
                        shortest = new_path
        return shortest


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
        for i in graph_obj.find_shortest_path(adj_list, start_home, end_home):
            gift_count[i] = gift_count.setdefault(i, 0) + 1
    print(max(gift_count.values()))


if __name__ == "__main__":
    main()
