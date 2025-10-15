class Solution(object):
    def __init__(self):
        self.letter_map = {
            "0": "",
            "1": '',
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

    def letter_combination(self, digits):
        if not digits:
            return []
        res = []

        self.backtrack(digits, 0, res, [])
        return res

    def backtrack(self, _digits, index, _res, path):
        if index == len(_digits):
            _res.append(''.join(path[:]))
            return
        nums = self.letter_map[_digits[index]]

        for n in nums:
            path.append(n)
            self.backtrack(_digits, index + 1, _res, path)
            path.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.letter_combination("2"))
