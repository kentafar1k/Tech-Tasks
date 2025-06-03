arr = [5, 2, 4, 1, 6]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr  # База рекурсии

    pivot = arr[0]  # Опорный элемент (всегда индекс 0)
    left = [x for x in arr[1:] if x < pivot]       # Меньше pivot
    right = [x for x in arr[1:] if x >= pivot]     # Больше или равны

    return quick_sort(left) + [pivot] + quick_sort(right)


print(arr)
print(quick_sort(arr))