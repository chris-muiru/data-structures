def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    midpoint = len(list) // 2

    if list[midpoint] == target:
        return True
    elif list[midpoint] < target:
        return recursive_binary_search(list[midpoint + 1 :], target)
    elif list[midpoint] > target:
        return recursive_binary_search(list[:midpoint], target)


def verify(result):
    print("Result is ", result)


numbers = [1, 2, 3, 4, 5]
target = 5

verify(recursive_binary_search(numbers, target))
