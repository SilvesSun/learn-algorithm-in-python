from pprint import pprint


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """

    # 每块的大小size = numRows + numRows -2
    size = numRows * 2 - 2
    if size == 0:
        return s

    # 需要生成的块数为
    count = -1
    length = len(s)
    if length % size == 0:
        count = length / size
    else:
        count = length / size + 1

    s += (size - length % size) * ' '
    matrix = []
    for i in range(int(count)):
        matrix.append(s[size*i:size*i+size])
        # print(matrix)
    new_s = []
    for item in matrix:
        list1 = list(item[:numRows])
        # print(list1)
        pprint(item[numRows:size].center(numRows))
        list2 = list(item[numRows:size].center(numRows))[::-1]
        print(list2)
        new_s.append(list1)
        new_s.append(list2)
    s1 = ''
    for i in range(numRows):
        for j in new_s:
            s1 += j[i]

    return s1.replace(' ', '')
convert('ABCD', 3)