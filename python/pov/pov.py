from json import dumps

class Tree:
    def __init__(self, label, children=None):
        self.label = label
        self.children = children if children is not None else []

    def __dict__(self):
        return {self.label: [c.__dict__() for c in sorted(self.children)]}

    def __str__(self, indent=None):
        return dumps(self.__dict__(), indent=indent)

    def __lt__(self, other):
        return self.label < other.label

    def __eq__(self, other):
        if not isinstance(other, Tree):
            return False
        return self.__dict__() == other.__dict__()

    def from_pov(self, from_node):
        def find_path(current, target, path=None):
            if path is None:
                path = []
            if current.label == target:
                return path + [current]
            for child in current.children:
                result = find_path(child, target, path + [current])
                if result:
                    return result
            return None

        path = find_path(self, from_node)
        if not path:
            raise ValueError("Tree could not be reoriented")

        # If it's a singleton tree, just return a copy of it
        if len(path) == 1:
            return Tree(from_node)

        new_root = Tree(from_node)
        current = new_root
        for node in reversed(path[:-1]):
            new_node = Tree(node.label)
            current.children.append(new_node)
            for child in node.children:
                if child.label != path[path.index(node) + 1].label:
                    new_node.children.append(Tree(child.label, child.children))
            current = new_node

        # Move original children of the new root
        if len(path) > 1:
            original_children = [child for child in path[-2].children if child.label == from_node][0].children
            for child in original_children:
                new_root.children.append(Tree(child.label, child.children))

        return new_root

    def path_to(self, from_node, to_node):
        if from_node == to_node:
            return [from_node]

        reoriented = self.from_pov(from_node)

        def find_path(current, target, path=None):
            if path is None:
                path = []
            if current.label == target:
                return path + [current.label]
            for child in current.children:
                result = find_path(child, target, path + [current.label])
                if result:
                    return result
            return None

        path = find_path(reoriented, to_node)

        if not path:
            raise ValueError("No path found")

        return path