class Solution(object):

    def isAdditiveNumber(self, num):
        if len(num) < 3:
            return False
        path = []
        res = self.backtrack(num, 0, path, '')
        # print(path)
        return res

    def backtrack(self, num, idx, path, tmp_str):
        if len(path) > 2 and path[-1] != path[-2] + path[-3]:
            return False
        if idx == len(num) and len(path) > 2:
            return True
        for i in range(idx, len(num)):
            if num[idx] == '0' and i > idx:
                return False
            tmp_str += num[i]
            print(i, tmp_str, path)
            path.append(int(tmp_str))
            if self.backtrack(num, i + 1, path, ''):
                return True
            path.pop()
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isAdditiveNumber('199100199'))
