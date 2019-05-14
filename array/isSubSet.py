"""
判断两个升序数组其中一个是另外一个数组的子集，需要满足以下两个条件：
- 数组N的所有元素都能在数组M中找到；
- 数组N项中元素重复项的个数不能大于数组M中元素重复项的个数。
"""


class Solution(object):
    def is_subset(self, arr1, arr2):
        m = len(arr1)
        n = len(arr2)
        i = 0
        j = 0
        while m > n and i < m and j < n:
            if arr1[i] < arr2[j]:
                i += 1
            elif arr1[i] > arr2[j]:  # arr2 的重复项大于arr1, 或者从某项开始不相等
                return False
            else:
                i += 1
                j += 1
            print(i, j)

        if j < n:
            return False
        else:
            return True


a = [1, 2, 3, 3, 4, 5, 5]
b = [2, 3, 3, 3, 5]

s = Solution()
print(s.is_subset(a, b))
