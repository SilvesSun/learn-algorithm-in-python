"""
给定一个字符串，里面只包含 R、G、B 三个字符，请给这个字符串排序，要求最终结果的顺序是所有R在最前面，所有G在中间，所有B在最后
"""


def solve(s):
    left, cur, right = 0, 0, len(s) - 1
    s_list = list(s)
    while cur <= right:
        if s_list[cur] == 'R':
            s_list[left], s_list[cur] = s_list[cur], s_list[left]
            left += 1
            cur += 1
        elif s_list[cur] == 'G':
            cur += 1
        else:
            s_list[cur], s_list[right] = s_list[right], s_list[cur]
            right -= 1
        print(cur, s_list)
    return ''.join(s_list)


s = "GBRR"
solve(s)
