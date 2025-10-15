class Solution(object):
    def __init__(self):
        self.times = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32]
        self.hours = []
        self.mins = []

    def read_binary_watch(self, turned_on):
        res = []
        self.backtrack(turned_on, 0, res)
        return res

    def backtrack(self, n, i, ls):
        """
        @param light_num: 当前亮着的灯
        """
        if len(self.hours) + len(self.mins) >= n:
            hour = sum(self.hours)
            if hour > 11:
                return
            minute = sum(self.mins)
            if minute > 59:
                return
            if minute > 0:
                if minute < 10:
                    ls.append(f"{hour}:0{minute}")
                else:
                    ls.append(f"{hour}:{minute}")
            else:
                ls.append(f"{hour}:00")
            # self.mins = []
            # self.hours = []
            return
        if len(self.hours) > 4: return
        if len(self.mins) > 6: return

        for j in range(i, len(self.times)):
            # print(i)
            if j < 4:
                self.hours.append(self.times[j])
            else:
                self.mins.append(self.times[j])
            self.backtrack(n, j + 1, ls)
            if j < 4:
                self.hours.pop()
            else:
                self.mins.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.read_binary_watch(7))
