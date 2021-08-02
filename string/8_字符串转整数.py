class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        start = s[0]
        negative = False
        if start == '-':
            negative = True
        s1 = ''
        if start in ['-', '+']:
            s1 = s[1:]
        else:
            s1 = s
        if not s1: return 0
        if not s1[0].isdigit(): return 0
        i = 0
        v = ''
        for i in range(len(s1)):
            if s1[i].isdigit():
                v += s1[i]
            else:
                break
        if not v: return 0
        num = int(v) if not negative else -int(v)
        return num


if __name__ == '__main__':
    s = '42'
    print(Solution().myAtoi(s))