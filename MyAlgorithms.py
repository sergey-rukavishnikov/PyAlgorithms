def insertion_sort(arr, comp_func):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
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
