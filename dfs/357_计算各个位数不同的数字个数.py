class Solution(object):
    def __init__(self):
        self.total = 0

    def count_numbers_with_unique_digits(self, n):
        if n == 0:
            return 1

        used = [False for _ in range(10)]

        def backtrack(n, idx):
            count = 0
            if idx != n:
                for i in range(10):
                    if i == 0 and n > 1 and idx == 1:
                        continue
                    if used[i]:
                        continue
                    used[i] = True
                    count += backtrack(n, idx + 1) + 1
                    used[i] = False
            return count

        return backtrack(min(10, n), 0)

    def count_numbers_with_unique_digits_2(self, n):
        if n == 0: return 1
        used = [False for _ in range(10)]

        def dfs(n, idx):
            if n == idx: return
            for i in range(10):
                if used[i]: continue
                used[i] = True
                self.total += 1
                if i != 0 or idx > 0:
                    dfs(n, idx + 1)
                used[i] = False

        dfs(n, 0)
        return self.total


if __name__ == '__main__':
    s = Solution()
    print(s.count_numbers_with_unique_digits_2(3))
