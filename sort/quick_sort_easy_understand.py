# coding=utf-8
def quick_sort(alist):
    """
    这种写法需要额外的空间, 但是易于理解
    :param alist:
    :return:
    """
    # 首先初始化三个列表分别存放小于,大于基础值的数值
    less = []
    more = []
    equal = []
    if len(alist) <= 1:
        return alist
    else:
        base = alist[0]
        for i in alist:
            if i < base:
                less.append(i)
            elif i > base:
                more.append(i)
            else:
                equal.append(i)

        less = quick_sort(less)
        more = quick_sort(more)

        return less + equal + more


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
alist = quick_sort(alist)
print(alist)
