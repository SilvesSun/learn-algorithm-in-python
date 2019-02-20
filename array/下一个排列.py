class Solution(object):
    def nextPermutation(self, nums):
        """
        :type numss: List[int]
        :rtype: void Do not return anything, modify numss in-place instead.
        比如排列是(2,3,6,5,4,1)，求下一个排列的基本步骤是这样：

        先从后往前找到第一个不是依次增长的数，记录下位置p。比如例子中的3，对应的位置是1;
        接下来分两种情况：
        (1) 如果上面的数字都是依次增长的，那么说明这是最后一个排列，下一个就是第一个，其实把所有数字反转过来即可(比如(6,5,4,3,2,1)下一个是(1,2,3,4,5,6));
        (2) 否则，如果p存在，从p开始往后找，找到下一个数就比p对应的数大的数字，然后两个调换位置，比如例子中的4。调换位置后得到(2,4,6,5,3,1)。最后把p之后的所有数字倒序，比如例子中得到(2,4,1,3,5,6), 这个即是要求的下一个排列。

        """

        partition = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                partition = i
                break

        if partition == -1:
            nums.reverse()
            return
        else:
            for i in range(len(nums) - 1, partition, -1):
                if nums[i] > nums[partition]:
                    nums[i], nums[partition] = nums[partition], nums[i]
                    break
        left = partition + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1


s = Solution()

nums = [3, 2, 1]
s.nextPermutation(nums)
