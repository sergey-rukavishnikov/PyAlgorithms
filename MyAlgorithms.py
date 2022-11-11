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


help(insertion_sort.__doc__)