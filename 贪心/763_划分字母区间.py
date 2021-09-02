# 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。
#
#
#
#  示例：
#
#
# 输入：S = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca", "defegde", "hijhklij"。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
#
#
#
#
#  提示：
#
#
#  S的长度在[1, 500]之间。
#  S只包含小写字母 'a' 到 'z' 。
#
#  Related Topics 贪心 哈希表 双指针 字符串
#  👍 554 👎 0
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        idx_map = {}
        for idx, i in enumerate(s):
            if i not in idx_map: idx_map[i] = [idx]
            else: idx_map[i].append(idx)
        n = len(s)
        res = []
        start = 0
        print(idx_map)
        while start < n:
            end = idx_map[s[start]][-1]
            tmp = s[start: end+1]
            tn = len(tmp)
            _idx = 0
            while _idx < tn:
                _end = idx_map[s[start+_idx]][-1]
                if _end > end:
                    end = _end
                    tmp = s[start: end+1]
                    tn = len(tmp)
                _idx += 1
            res.append(tmp)
            start = end + 1
        return [len(i) for i in res]


if __name__ == '__main__':
    print(Solution().partitionLabels('ababcbacadefegdehijhklij'))