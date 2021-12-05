# coding:utf-8
__date__ = '2018/11/16 11:18'


def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count - 1):
        for j in range(0, count - 1):
            if lists[j] > lists[j + 1]:
                lists[j], lists[j + 1] = lists[j + 1], lists[j]
    return lists


# 优化版本
# 优化3：上面写的算法只适合比较number或者string类型，如果要比较对象呢，就不适合了，所有可以传入一个比较函数，将算法函数变成高阶函数，就更具有通用性。
# 优化4：我们知道上面的函数在运行完成之后，原来传进去的列表顺序就改变了，产生了副作用，那么我们是不是应该尽量减少副作用，以便原来的列表还可以进行其他操作。这里用切片。

def _bubble_sort(lists):
    n = len(lists)
    for i in range(n - 1):
        swap = False
        for j in range(n - 1 - i):  # 1, 每次循环， 就排好了一个元素， 减少比较次数
            if lists[j] > lists[j + 1]:
                lists[j + 1], lists[j] = lists[j], lists[j + 1]
                swap = True
        if not swap:  # 优化2： 已经排好序就提前停止算法
            break


print(bubble_sort([54, 26, 93, 17, 77, 31, 44, 55, 20]))
