def select_sort(alist):
    n = len(alist)
    for i in range(n-1):
        for j in range(i+1, n):
            if alist[j] < alist[i]:
                alist[i], alist[j] = alist[j], alist[i]


alist = [12, 2, 34, 78, 6]
select_sort(alist)
print(alist)
