def append(list1, list2):
    return list1 + list2

def concat(lists):
    flattened_list = []
    for nested_list in lists:
        flattened_list.extend(nested_list)
    return flattened_list

def filter(function, lists):
    result = []
    for item in lists:
        if function(item) is True:
            result.append(item)
    return result


def length(list):
    return len(list)


def map(function, list):
    result = []
    for item in list:
        result.append(function(item))
    return result


def foldl(function, list, initial):
    accumulator = initial
    for element in list:
        accumulator = function(accumulator, element)
    return accumulator


def foldr(function, list, initial):
    accumulator = initial
    for element in reversed(list):
        accumulator = function(accumulator, element)
    return accumulator


def reverse(list):
    return list[::-1]
