class Solution(object):
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


if __name__ == '__main__':
    s = Solution()
    print(s.count_numbers_with_unique_digits(2))
