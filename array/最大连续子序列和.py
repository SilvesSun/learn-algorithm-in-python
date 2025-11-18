"""
Divide-and-Conquer
any contiguous subarray AOEi : : j 
of AOElow : : high must lie in exactly one of the following places:
- entirely in the subarray AOElow : : mid, so that low  i  j  mid,
-  entirely in the subarray AOEmid C 1 : : high, so that mid < i  j  high, or
- crossing the midpoint, so that low  i  mid < j  high.
"""


def max_subarray_sum(array):
    length = len(array)
    if len(array) <= 1:
        return array[0]
    mid = length // 2
    left = array[:mid]
    right = array[mid:]
    max_left = max_subarray_sum(left)
    max_right = max_subarray_sum(right)
    left_sum = 0
    _sum = 0
    for i in range(mid, 0, -1):
        _sum += array[i]
        if _sum > left_sum:
            left_sum = _sum

    right_sum = 0
    _sum = 0
    for i in range(mid+1, length):
        _sum += array[i]
        if _sum > right_sum:
            right_sum = _sum
    max_cross = left_sum + right_sum

    return max(max_left, max_right, max_cross)


print(max_subarray_sum([-2, 11, -4, 13, -5, -2]))
