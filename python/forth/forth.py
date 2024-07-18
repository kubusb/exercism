class StackUnderflowError(Exception):
    pass

def evaluate(input_data):
    if isinstance(input_data, list):
        input_data = " ".join(input_data)

    stack = []
    words = {}
    word_versions = {}

    def binary_op(op):
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")
        y = stack.pop()
        x = stack.pop()
        stack.append(op(x, y))

    def dup():
        if len(stack) < 1:
            raise StackUnderflowError("Insufficient number of items in stack")
        stack.append(stack[-1])

    def drop():
        if len(stack) < 1:
            raise StackUnderflowError("Insufficient number of items in stack")
        stack.pop()

    def swap():
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")
        x, y = stack.pop(), stack.pop()
        stack.append(x)
        stack.append(y)

    def over():
        if len(stack) < 2:
            raise StackUnderflowError("Insufficient number of items in stack")
        stack.append(stack[-2])

    def define_word(word_name, definition):
        if word_name.isdigit() or (word_name[0] == "-" and word_name[1:].isdigit()):
            raise ValueError("illegal operation")
        if word_name in word_versions:
            word_versions[word_name] += 1
        else:
            word_versions[word_name] = 0
        words[word_name, word_versions[word_name]] = definition

    def execute_word(word, version, call_stack):
        if (word, version) in call_stack:
            if version > 0:
                execute_word(word, version - 1, call_stack)
            return
        call_stack.add((word, version))
        for token in words[word, version]:
            process_token(token, call_stack, version)
        call_stack.remove((word, version))

    def process_token(token, call_stack, current_version):
        if token.isdigit() or (token[0] == "-" and token[1:].isdigit()):
            stack.append(int(token))
        elif token in word_versions:
            if not call_stack:  # If it's the initial call, use the latest version
                execute_word(token, word_versions[token], set())
            else:
                execute_word(token, min(current_version, word_versions[token]), call_stack)
        elif token == "+":
            binary_op(lambda x, y: x + y)
        elif token == "-":
            binary_op(lambda x, y: x - y)
        elif token == "*":
            binary_op(lambda x, y: x * y)
        elif token == "/":
            try:
                binary_op(lambda x, y: x // y)
            except ZeroDivisionError:
                raise ZeroDivisionError("divide by zero")
        elif token == "DUP":
            dup()
        elif token == "DROP":
            drop()
        elif token == "SWAP":
            swap()
        elif token == "OVER":
            over()
        else:
            raise ValueError("undefined operation")

    tokens = input_data.upper().split()
    i = 0
    while i < len(tokens):
        if tokens[i] == ":":
            word_name = tokens[i + 1]
            definition = []
            i += 2
            while tokens[i] != ";":
                definition.append(tokens[i])
                i += 1
            define_word(word_name, definition)
        else:
            process_token(tokens[i], set(), word_versions.get(tokens[i], 0))
        i += 1

    return stack