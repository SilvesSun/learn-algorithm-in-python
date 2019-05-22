"""
第一次遍历从后向前，找出第 i 个元素右边元素的最小值，
保存在 rightMin 数组中。第二次遍历，从前向后，使用一个临时变量保存左边元素的最大值。一边判断一边更新
"""


def solve(nums):
    r_min_arr = [_ for _ in range(len(nums))]
    l = len(nums)
    r_min = nums[l - 1]
    for i in range(l - 1, -1, -1):
        r_min_arr[i] = min(r_min, nums[i])
    print(r_min_arr)

    l_max = nums[0]
    for j in range(0, l-1):
        if nums[j] > l_max:
            l_max = nums[j]
            if nums[j] < r_min_arr[j+1]:
                print(nums[j])


if __name__ == '__main__':
    solve([1, 8, 6, 9, 10, 15, 21, 20])
