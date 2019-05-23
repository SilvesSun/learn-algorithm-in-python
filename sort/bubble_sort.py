# coding:utf-8
__date__ = '2018/11/16 11:18'


def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


print(bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
