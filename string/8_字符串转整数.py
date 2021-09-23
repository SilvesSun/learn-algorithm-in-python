class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s: return 0
        l = False
        if s[0] == '-':
            l = True
            s = s[1:]
        if not s[0].isdigit(): return 0
        i = 0

        while i < len(s):
            if s[i].isdigit():
                i += 1
            else:
                break
        return -int(s[:i + 1]) if l else int(s[:i + 1])

if __name__ == '__main__':
    print(Solution().myAtoi(' -42'))