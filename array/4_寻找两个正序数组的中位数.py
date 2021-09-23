class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        total = m + n
        if total % 2 == 1:
            # 奇数， k = (n + 1) // 2
            return self.get_kth_elem(nums1, nums2, (total + 1) // 2)
        else:
            return (self.get_kth_elem(nums1, nums2, (total + 2) // 2) + self.get_kth_elem(nums1, nums2, total // 2)) / 2

    def get_kth_elem(self, nums1, nums2, k):
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
        if len(nums2) == 0:
            return nums1[k - 1]
        if k == 1:
            return min(nums1[0], nums2[0])
        t = min(k // 2, len(nums2))
        if nums1[t - 1] >= nums2[t - 1]:
            return self.get_kth_elem(nums1, nums2[t:], k - t)
        else:
            return self.get_kth_elem(nums1[t:], nums2, k - t)


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print(Solution().findMedianSortedArrays(nums1, nums2))
