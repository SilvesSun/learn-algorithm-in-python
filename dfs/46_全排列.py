class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return

        res = []

        def backtrack(_nums, track):
            if not _nums:
                res.append(track[:])
                return
            for i in range(len(_nums)):
                track.append(_nums[i])
                backtrack(_nums[:i] + _nums[i+1:], track)
                track.pop()

        backtrack(nums, [])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))