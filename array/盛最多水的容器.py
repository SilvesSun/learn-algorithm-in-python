class Solution(object):
    def maxArea1(self, height):
        """
        :type height: List[int]
        :rtype: int
        暴力遍历
        """
        maxA = 0
        for i in range(0, len(height) - 1):
            for j in range(i, len(height)):
                area = (j - i) * min(height[i], height[j])
                maxA = max(area, maxA)
        print(maxA)
        return maxA

    def maxArea2(self, height):
        # 双指针法, 移动较小的指针

        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            area = (r - l) * min(height[l], height[r])
            if area > res:
                res = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


s = Solution()
s.maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7])
