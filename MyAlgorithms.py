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


def merge(arr1, arr2, comp_func=None):
    """

    :param arr1:
    :param arr2:
    :param comp_func:
    :return:
    """
    destination = []
    i = j = 0
    len1 = len(arr1)
    len2 = len(arr2)
    if comp_func is None:
        while i < len1 and j < len2:
            if arr1[i] < arr2[j]:
                destination.append(arr1[i])
                i += 1
            else:
                destination.append(arr2[j])
                j += 1
        if i == len1:
            while j < len2:
                destination.append(arr2[j])
                j += 1
        else:
            while i < len1:
                destination.append(arr1[i])
                i += 1
    else:
        while i < len1 and j < len2:
            if comp_func(arr2[i], arr2[j]):
                destination.append(arr1[i])
                i += 1
            else:
                destination.append(arr2[j])
                j += 1
        if i == len1:
            while j < len2:
                destination.append(arr2[j])
                j += 1
        else:
            while i < len1:
                destination.append(arr1[i])
                i += 1
    return destination


def merge_sort(array, comp_func=None, bot=0, top=None):
    """

    :param array:
    :param comp_func:
    :param bot:
    :param top:
    :return:
    """
    if top is None:
        top = len(array)
    if bot < top:
        mid = math.floor((bot + top) / 2)
        merge_sort(array, bot=bot, top=mid)
        merge_sort(array, bot=mid + 1, top=top)
        array[bot:top + 1] = merge(array[bot:mid + 1], array[mid + 1:top + 1], comp_func=comp_func)


def binary_search(arr, des_el):
    """

    :param arr:
    :param des_el:
    :return:
    """
    bot = 0
    top = len(arr) - 1
    if arr[bot] > des_el or arr[top] < des_el:
        return None
    mid = math.floor((bot + top) / 2)
    while arr[mid] != des_el and bot != top:
        if mid >= des_el:
            top = mid
        else:
            bot = mid
        mid = math.floor((bot + top) / 2)
    if arr[mid] == des_el:
        return mid
    else:
        return None
    pass
