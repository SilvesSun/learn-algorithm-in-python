class Solution:
    nums: list

    def shuffle(self) -> List[int]:
        """
        fish-yates shuffle算法
        """
        for i in range(len(self.nums)):
            j = random.randrange(i, len(self.nums))
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums
