import sys
sys.path.append('..')
import common


def read_edges(fpath):

    def parse_line(line):
        return tuple(line.strip().split('-'))

    with open(fpath) as f:
        return list(map(parse_line, f.readlines()))


def graph_to_tree(graph):

    paths = []

    def fill(tree_node):

        if tree_node.value == 'end':
            paths.append(tree_node.get_path())
            return

        for child_node in tree_node.children:
            if child_node.value in graph.adj:
                child_node.add_children(graph.adj[child_node.value])
                fill(child_node)

    tree = TreeNode('start')
    tree.add_children(graph.adj['start'])
    fill(tree)

    return tree, paths


class TreeNode:
    
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent
        self.children = []
        
        if parent is None:
            self.seen = set()
        else:
            self.seen = parent.seen.copy()

        if value.islower():
            self.seen.add(value)


    def add_children(self, children):
        
        for c in children:
            
            if c in self.seen:
                continue

            child_node = TreeNode(c, self)
            self.children.append(child_node)

    def get_path(self):
        path_reversed = [self.value, ]
        node = self.parent
        while node is not None:
            path_reversed.append(node.value)
            node = node.parent

        return list(reversed(path_reversed))


class Graph:
    
    def __init__(self, edges):
        self.adj = {}
        for a, b in edges:
            self._add_edge(a, b)
            self._add_edge(b, a)

    def _add_edge(self, a, b):
        if a not in self.adj:
            self.adj[a] = [b, ]
        else:
            self.adj[a].append(b)


if __name__ == '__main__':

    fpath = common.file_path('input.txt')
    edges = read_edges(fpath)
    graph = Graph(edges)

    tree, paths = graph_to_tree(graph)
    result = len(paths)

    assert result == 3485

    print(f'Number of paths: {result}')