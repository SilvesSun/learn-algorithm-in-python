# coding:utf-8


# 定义冲突
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        # 如果下一个皇后和正在考虑的前一个皇后的水平距离为0(列相同)或者等于垂直距离(在一条对角线上), 就会发生冲突
        if abs(state[i] - nextX) in (0, nextY - i):
            return True
    return False


def queens(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1:
                yield (pos,)
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'x ' + '. ' * (length-pos-1)

    for pos in solution:
        print(line(pos))


