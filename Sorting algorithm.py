def find_min_index(a, start, end):
    index = start
    for i in range(start, end):
        if a[i] < a[index]:
            index = i
    return index


def selection_sort(a, n):
    for i in range(n):
        value_store = a[i]
        index_of_min = find_min_index(a, i, n)
        a[i] = a[index_of_min]
        a[index_of_min] = value_store
    return a


def recursive_selection_sort(a, start, end):
    if start < end:
        index_of_min = find_min_index(a, start, end)
        value_store = a[start]
        a[start] = a[index_of_min]
        a[index_of_min] = value_store
    return a


array = [3, 6, 1, 4, 5]

print(selection_sort(array, len(array)))
print(recursive_selection_sort(array, 0, len(array)))
