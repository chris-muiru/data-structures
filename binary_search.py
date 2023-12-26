def binary_search(list, target):
    """returns the index position of target if found else returns None

    Args:
        list (_type_): list to be searched
        target (_type_): target to search for
    """
    first = 0  # O(n)
    last = len(list) - 1

    while first <= last:  # 0(log n)
        midPoint = (first + last) // 2  # floor division
        if list[midPoint] == target:  # 0(1)
            return midPoint
        elif list[midPoint] < target:
            first = midPoint + 1
        else:
            last = midPoint - 1
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


# for binary search,values should be sorted
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


target = 10

verify(binary_search(numbers, target))
