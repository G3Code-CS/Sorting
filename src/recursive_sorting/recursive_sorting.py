# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [] * elements
    # TO-DO
    while (len(arrA) and len(arrB)):
        if (arrA[0] < arrB[0]):
            merged_arr.append(arrA.pop(0))
            # print(arrA)
        else:
            merged_arr.append(arrB.pop(0))
            # print(arrB)
    while (len(arrA)):
        merged_arr.append(arrA.pop(0))
    while (len(arrB)):
        merged_arr.append(arrB.pop(0))

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # TO-DO
    if (len(arr) < 2):
        return arr
    arrLen = len(arr)
    midVal = arrLen//2
    arrA = [i for i in arr[0:midVal]]
    arrB = [i for i in arr[midVal:arrLen]]
    # print(arrA, arrB)
    return merge(merge_sort(arrA),  merge_sort(arrB))


# arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
# print(merge_sort(arr1))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
