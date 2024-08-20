class Zipper:
    def __init__(self, tree, path=None):
        self.tree = tree
        self.path = path or []

    @staticmethod
    def from_tree(tree):
        return Zipper(tree)

    def value(self):
        return self.tree["value"]

    def set_value(self, value):
        new_tree = dict(self.tree)
        new_tree["value"] = value
        return Zipper(new_tree, self.path)

    def left(self):
        if self.tree["left"] is None:
            return None
        return Zipper(self.tree["left"], self.path + [("left", self.tree)])

    def set_left(self, left):
        new_tree = dict(self.tree)
        new_tree["left"] = left
        return Zipper(new_tree, self.path)

    def right(self):
        if self.tree["right"] is None:
            return None
        return Zipper(self.tree["right"], self.path + [("right", self.tree)])

    def set_right(self, right):
        new_tree = dict(self.tree)
        new_tree["right"] = right
        return Zipper(new_tree, self.path)

    def up(self):
        if not self.path:
            return None
        direction, parent = self.path[-1]
        new_parent = dict(parent)
        new_parent[direction] = self.tree
        return Zipper(new_parent, self.path[:-1])

    def to_tree(self):
        zipper = self
        while zipper.path:
            zipper = zipper.up()
        return zipper.tree