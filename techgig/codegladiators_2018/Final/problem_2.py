from functools import reduce


class Problem(object):
    def __init__(self, *args, **kwargs):
        pass

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

    def find_all_paths(self, graph, start, end, path=[]):
        """
        find all paths from one node to other in given graph
        :param graph: graph structure
        :param start: start node
        :param end: end node
        :param path: explored path between start and end nodes
        :return: all explored paths
        """
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
                    paths.append(new_path)  # add new path to list instead of returning it.
        return paths

    def get_path(self, graph, start, path=[]):
        for ends in graph[start]:
            path = path + [start]
            for target in ends:
                if start in graph[target]:
                    path = path + [start]
                    return [path]
            paths = []  # maintain a list to store all explored path
            for node in graph[start]:
                if node not in path:
                    new_paths = self.get_path(graph, path)
                    for new_path in new_paths:
                        paths.append(new_path)  # add new path to list instead of returning it.
            return paths


def main():
    p = Problem()
    hills, roads = map(int, input().split())
    road_map = {}
    cost_map = {}
    cyclic_paths = []
    for _ in range(roads):
        hill_src, hill_dest, t, h = map(int, input().split())
        cost_map[(hill_src, hill_dest)] = [t, h]
        if hill_src in road_map:
            road_map[hill_src].append(hill_dest)
        else:
            road_map[hill_src] = [hill_dest]
    # print(road_map)
    # constructing cyclic paths... need alternative
    for hill in road_map.keys():
        for hill_d in road_map.keys():
            if hill is not hill_d:
                paths = p.find_all_paths(road_map, hill, hill_d)
                if paths:
                    for path in paths:
                        if hill in road_map[path[-1]]:
                            cyclic_paths.append(path + [hill])
    # cyclic_paths = p.get_path(road_map)
    # print(cyclic_paths)
    cyclic_paths = sorted(cyclic_paths, key=lambda x: len(x))
    min_road = len(cyclic_paths[0])
    min_roads = [p for p in cyclic_paths if len(p) is min_road]
    costs = []
    for path in min_roads:
        cost = 0
        for i in range(min_road-1):
            x, y = path[i], path[i+1]
            cost += cost_map[(x, y)][1] - cost_map[(x, y)][0]
        costs.append(cost)
    return "{} {}".format(min_road-1, max(costs))


if __name__ == "__main__":
    print(main())
