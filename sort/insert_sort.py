# coding=utf-8
def insert_sort(_list):
    """
    插入排序的时间复杂度为O(n^2), 最好的情况为O(n)
    :param _list:
    :return:
    """
    for index in range(_list):
        current = _list[index]
        position = index
        while position > 0 and _list[position-1] > current:
            _list[position] = _list[position-1]
            position -= 1
        _list[position] = current
