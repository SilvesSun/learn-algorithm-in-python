def merge_sort(nums, left, right):
    # 1.确定分界点
    # 2 递归排序
    # 3 归并合二为一
    # 归并排序是先分再归并
    if left >= right: return
    mid = (left + right) >> 1
    merge_sort(nums, left, mid)
    merge_sort(nums, mid + 1, right)
    res = []
    i = left
    j = mid + 1
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            res.append(nums[i])
            i += 1
        else:
            res.append(nums[j])
            j += 1
    res.extend(nums[i:mid + 1])
    res.extend(nums[j:right + 1])
    nums[left:right + 1] = res
    print(res)


nums = [5, 4, 2, 1, 3, 3, 4, 10]

merge_sort(nums, 0, len(nums) - 1)
