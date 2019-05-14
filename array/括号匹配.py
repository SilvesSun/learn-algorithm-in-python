def match_brackets(str):
    symbol = {'}': '{', ']': '[', ')': '('}
    l, r = symbol.values(), symbol.keys()

    arr = []
    for i in str:
        if i in l:
            arr.append(i)
        elif i in r:
            if arr and arr[-1] == symbol[i]:
                arr.pop()
            else:
                return False
    return not arr


print(match_brackets("3 * {3 +[(2 -3) * (4+5)]}"))
print(match_brackets("3 * {3+ [4 - 6}]"))
