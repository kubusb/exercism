def flatten(iterable):
    flattened_list = []

    for item in iterable:
        if item is None:
            continue
        if isinstance(item, list):
            flattened_list.extend(flatten(item))
        else:
            flattened_list.append(item)

    return flattened_list