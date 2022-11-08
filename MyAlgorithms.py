def insertion_sort(arr, comp_func=None):
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
