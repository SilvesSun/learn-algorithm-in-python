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


def insert_sort2(_list):
    for i in range(len(_list)-1):
        for j in range(i+1, len(_list)):
            if _list[i] > _list[j]:
                _list[i], _list[j] = _list[j], _list[i]
    return _list


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert_sort2(alist)
print(alist)