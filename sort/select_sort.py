def select_sort(alist):
    n = len(alist)
    for i in range(0, n):
        min = i
        for j in range(i + 1, n):
            if alist[j] < alist[min]:
                min = j
                alist[min], alist[i] = alist[i], alist[min]
    return alist


alist = [12, 2, 34, 78, 6]
select_sort(alist)
print(alist)
