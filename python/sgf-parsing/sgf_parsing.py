class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        if self.properties != other.properties:
            return False
        if len(self.children) != len(other.children):
            return False
        return all(child == other_child for child, other_child in zip(self.children, other.children))

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    def parse_property_value(s, i):
        value = ""
        while i < len(s) and s[i] != ']':
            if s[i] == '\\':
                i += 1
                if i < len(s):
                    if s[i] == '\n':
                        i += 1  # Skip escaped newline
                    elif s[i] == '\t':
                        value += ' '  # Convert escaped tab to space
                        i += 1
                    else:
                        value += s[i]  # Keep other escaped characters as-is
                        i += 1
            elif s[i] == '\t':
                value += ' '  # Convert unescaped tab to space
                i += 1
            else:
                value += s[i]
                i += 1
        return value, i

    def parse_properties(s, i):
        properties = {}
        while i < len(s) and s[i] != ')' and s[i] != '(' and s[i] != ';':
            key = ''
            while i < len(s) and s[i] != '[':
                key += s[i]
                i += 1
            if not key.isupper():
                raise ValueError("property must be in uppercase")
            if i == len(s) or s[i] != '[':
                raise ValueError("properties without delimiter")
            values = []
            while i < len(s) and s[i] == '[':
                i += 1
                value, i = parse_property_value(s, i)
                if i == len(s) or s[i] != ']':
                    raise ValueError("property without closing bracket")
                values.append(value)
                i += 1
            properties[key] = values
        return properties, i

    def parse_node(s, i):
        if i >= len(s) or s[i] != ';':
            raise ValueError("node must start with a semicolon")
        i += 1
        properties, i = parse_properties(s, i)
        return SgfTree(properties), i

    def parse_tree(s, i):
        if i >= len(s) or s[i] != '(':
            raise ValueError("tree missing")
        i += 1
        nodes = []
        while i < len(s) and s[i] != ')':
            if s[i] == ';':
                node, i = parse_node(s, i)
                nodes.append(node)
            elif s[i] == '(':
                child_tree, i = parse_tree(s, i)
                if nodes:
                    nodes[-1].children.append(child_tree)
                else:
                    raise ValueError("child tree without parent")
            else:
                i += 1
        if i >= len(s) or s[i] != ')':
            raise ValueError("tree missing closing parenthesis")
        if not nodes:
            raise ValueError("tree with no nodes")
        tree = nodes[0]
        for node in nodes[1:]:
            tree.children.append(node)
        return tree, i + 1

    input_string = input_string.strip()
    if not input_string:
        raise ValueError("tree missing")

    tree, i = parse_tree(input_string, 0)
    if i != len(input_string):
        raise ValueError("invalid input")

    return tree