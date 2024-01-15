def find(search_list, value):
    sorted_search_list = sorted(search_list)
    if len(sorted_search_list) == 0:
        raise ValueError("value not in array")
    if len(sorted_search_list) == 1:
        if sorted_search_list[0] == value:
            return search_list.index(value)
        raise ValueError("value not in array")
    if len(sorted_search_list) % 2 != 0 and len(sorted_search_list) > 1:
        middle_element = int(len(sorted_search_list) // 2 )
        if sorted_search_list[middle_element] == value:
            return search_list.index(value)
        if sorted_search_list[middle_element] > value:
            sorted_search_list = sorted_search_list[:middle_element]
            find(sorted_search_list, value)
        elif sorted_search_list[middle_element] < value:
            sorted_search_list = sorted_search_list[middle_element:]
            find(sorted_search_list, value)
    elif len(sorted_search_list) % 2 == 0 and len(sorted_search_list) > 1:
        middle_element = int(len(sorted_search_list) // 2 )
        if sorted_search_list[middle_element] > value:
            sorted_search_list = sorted_search_list[:middle_element]
            find(sorted_search_list, value)
        elif sorted_search_list[middle_element] < value:
            sorted_search_list = sorted_search_list[middle_element:]
            find(sorted_search_list, value)
    return search_list.index(value)
