import math


# STRETCH: implement Linear Search
def linear_search(arr, target):
    # TO-DO: add missing code
    for i in range(len(arr)):
        if (arr[i] == target):
            return i
    return -1   # not found


# STRETCH: write an iterative implementation of Binary Search
def binary_search(arr, target):
    arr.sort()
    print(arr)
    if len(arr) == 0:
        return -1  # array empty

    low = 0
    high = len(arr)-1
    middle = math.floor(len(arr)/2)
    if (target > arr[middle]):
        for i, num in enumerate(arr, start=middle-1):
            if (num == target):
                return i
    elif (target < arr[middle]):
        for i, num in enumerate(arr, start=low):
            if (i == middle+1):
                break
            if (num == target):
                return i
    elif (target == arr[middle]):
        return high/2

    return -1


# STRETCH: write a recursive implementation of Binary Search
def binary_search_recursive(arr, target, low, high):

    middle = (low+high)//2

    if len(arr) == 0:
        return -1  # array empty
    # TO-DO: add missing if/else statements, recursive calls