class Solution(object):
    def __init__(self):
        self.res = []

    def generate_parenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
            return self.res

        self.get_parenthesis("", n, n)
        return self.res

    def get_parenthesis(self, s, left, right):
        if left == 0 and right == 0:
            self.res.append(s)
            return

        if left == right:
            self.get_parenthesis(s + '(', left - 1, right)

        elif left < right:
            if left > 0:
                self.get_parenthesis(s + '(', left - 1, right)
            self.get_parenthesis(s + ')', left, right - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.generate_parenthesis(3))