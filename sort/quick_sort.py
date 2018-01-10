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


def quick_sort_helper(myList, start, end):
    # 判断low是否小于high,如果为false,直接返回
    if start < end:
        i, j = start, end
        # 设置基准数
        base = myList[i]

        while i < j:
            while (i < j) and (myList[j] >= base):
                j = j - 1

            myList[i] = myList[j]

            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        # 做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base

        # 递归前后半区
        quick_sort_helper(myList, start, i - 1)
        quick_sort_helper(myList, j + 1, end)
    return myList


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist)
print(alist)