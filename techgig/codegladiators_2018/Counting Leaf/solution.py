class Tree(object):
    def __init__(self, nodes, **kwargs):
        self.total_nodes = kwargs.get('total_nodes')
        self.nodes = nodes if nodes else [-1, 0, 0, 1, 1]
        self.tree = self.make_tree()
        # print(self.tree)

    def make_tree(self):
        tree = {-1: [0]}
        for i in range(self.total_nodes):
            _parent = self.nodes[i]
            tree.setdefault(_parent, []).append(i)
        return tree

    def recursive_pop(self, removal_nodes, dict_):
        if not removal_nodes:
            return dict_
        for i in removal_nodes:
            pop_ = dict_.pop(i) if i in dict_ else []
            if pop_:
                self.recursive_pop(pop_, dict_)
            else:
                return dict_

    def delete_node(self, node):
        _key = [k for k, v in self.tree.items() if [node] == v]
        self.tree.pop(_key[0]) if _key else False
        pop_items = self.tree.pop(node) if node in self.tree else []
        self.tree = self.recursive_pop(pop_items, self.tree)
        return self.tree

    def leafs(self):
        nodes = []
        for i in self.tree.values():
            nodes += i
        nodes = set(nodes)
        leaf_nodes = set()
        for i in nodes:
            if i not in self.tree:
                leaf_nodes.add(i)
        return leaf_nodes


def main():
    n = int(input())
    nodes = list(map(int, input().split()))
    node_to_del = int(input())
    # n = 5
    # nodes = [-1, 0, 0, 1, 1]
    # node_to_del = 1
    t = Tree(nodes, total_nodes=n)  # [-1, 0, 0, 1, 1]
    t.delete_node(node_to_del)
    leafs = t.leafs()
    leafs.remove(node_to_del)
    print(len(leafs))


if __name__ == "__main__":
    main()
