class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        l = list(s)
        res = []
        step = 2 * k
        sub_l = [l[i:i + step] for i in range(0, len(l), step)]
        for i in sub_l:
            if len(i) < k:
                res.extend(i[::-1])
            else:
                res.extend(i[:k][::-1] + i[k:])
        return ''.join(res)


if __name__ == '__main__':
    s = 'abcdefg'
    print(Solution().reverseStr(s, 2))