def linear_search(list,target):
    """returns the index position of target if found else returns 
    None

    Args:
        list (_type_): list to search
        target (_type_): target to search for
    """
    # linear time O(n)
    for index in range(0,len(list)):
        if list[index] == target:
            return index
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ",index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,7,8,9,10]
target = 10 

verify(linear_search(numbers,target))