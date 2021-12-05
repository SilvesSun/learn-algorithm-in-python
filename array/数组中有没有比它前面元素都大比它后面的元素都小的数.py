arr = [21, 11, 45, 56, 9, 66, 77, 89, 78, 68, 100, 120, 111]


def find(arr):
    right_min = []
    r_min = float('inf')
    for i in range(len(arr)-1, -1, -1):
        if arr[i] <= r_min:
            r_min = arr[i]
        right_min.append(r_min)
    print(right_min)

    left_max = []
    l_max = float('-inf')
    for i in range(0, len(arr)):
        if arr[i] >= l_max:
            l_max = arr[i]
        left_max.append(l_max)
    print(left_max)
    res = []
    reverse_right_min = right_min[::-1]
    for i in range(0, len(arr)):
        if left_max[i] == reverse_right_min[i]:
            res.append(left_max[i])
    print(res)
find(arr)