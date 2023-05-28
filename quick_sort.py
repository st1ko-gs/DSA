def quick_sort(lst):
    if len(lst) < 1:
        return lst
    else:
        pivot = lst[0]
        left = [i for i in lst[1:] if i <= pivot]
        right = [i for i in lst[1:] if i > pivot]

        return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort([4,32,5,1,6,1,5]))

