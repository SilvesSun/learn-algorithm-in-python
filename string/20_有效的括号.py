class Solution:
    def isValid(self, s: str) -> bool:
        d = {
            '{': '}',
            '(': ')',
            '[': ']',
            '?': '?'
        }
        q = ['?']
        for c in s:
            if c in d:
                q.append(c)
            elif d[q.pop()] != c:
                return False
        return len(q) == 1


if __name__ == '__main__':
    print(Solution().isValid('()[]{}'))
