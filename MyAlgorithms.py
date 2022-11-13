import math


def insertion_sort(arr, comp_func=None):
    """
    _worst-case performance: O(n^2)
    _best-case performance: O(n)
    _input numbers are sorted without additional memory
    :param arr: array to sort
    :param comp_func: comparison function, specified by which attribute array should be sorted
    :return: sorted array
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        if comp_func is None:
            while i >= 0 and arr[i] > key:
                arr[i + 1] = arr[i]
                i = i - 1
        else:
            while i >= 0 and comp_func(arr[i], key):
                arr[i + 1] = arr[i]
                i = i - 1
        arr[i + 1] = key
    return arr


def comp(a, b):
    if a <= b:
        return False
    else:
        return True
    pass


def merge(A, p, q, r):
    n_1 = q - p + 1
    n_2 = r - q
    left = []
    right = []
    for i in range(0, n_1):
        left.append(A[p + i])
    for j in range(0, n_2):
        right.append(A[q + j + 1])
    i = 0
    j = 0
    min_n = n_1 if n_1 <= n_2 else n_2
    for k in range(p, p + min_n):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
    for k in range(p + min_n, r + 1):
        if n_1 >= n_2:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
    pass


def merge_sort(A, p, r):
    # make p and r optional and add optional compare function
    if p < r:
        q = math.floor((p + r) / 2)
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
    pass


def binary_search(arr, des_el):
    bot = 0
    top = len(arr) - 1
    if arr[bot] > des_el or arr[top] < des_el:
        return None
    mid = math.floor((bot + top)/2)
    while arr[mid] != des_el and bot != top:
        if mid >= des_el:
            top = mid
        else:
            bot = mid
        mid = math.floor((bot + top)/2)
    if arr[mid] == des_el:
        return mid
    else:
        return None
    pass
