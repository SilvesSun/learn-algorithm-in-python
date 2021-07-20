# coding=utf-8
def quick_sort(alist):
    """
    快速排序的思想:
    首先确定一个基准, 比如alist[0], 然后用两个指针, 一个指向列表头, 一个指向尾. 然后将指针分别右移/左移, 分别遇到小于/大于基准的值停
    止, 交换元素, 然后继续直到左右指针相遇, 停止遍历. 这个时候的位置就是基准锁应该在的位置

    快速排序的时间复杂度平均为O(nlogn), 最坏为O(n^2)
    :param alist:
    :return:
    """
    quick_sort_helper(alist, 0, len(alist) - 1)


def helper(nums, left, right):
    # 比较模板的写法
    if left >= right: return
    i = left - 1
    j = right + 1
    base = nums[left]
    # 使用两个指针， 从开始和结尾向中间遍历

    while i < j:
        while 1:
            i += 1
            if nums[i] >= base: break
        while 1:
            j -= 1
            if nums[j] <= base: break
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]

    helper(nums, left, j)
    helper(nums, j + 1, right)


def quick_sort_helper(nums, start, end):
    # 判断low是否小于high,如果为false,直接返回
    if start < end:
        i, j = start, end
        # 设置基准数
        base = nums[i]

        while i < j:
            while (i < j) and (nums[j] >= base):
                j = j - 1

            nums[i] = nums[j]

            while (i < j) and (nums[i] <= base):
                i = i + 1
            nums[j] = nums[i]
        # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        nums[i] = base

        # 递归前后半区
        quick_sort_helper(nums, start, i - 1)
        quick_sort_helper(nums, j + 1, end)
    return nums


if __name__ == '__main__':
    helper([49, 59, 88, 37, 98, 97, 68, 54, 31, 3], 0, 9)
