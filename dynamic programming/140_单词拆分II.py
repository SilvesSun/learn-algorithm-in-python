# 给定一个字符串 s 和一个字符串字典 wordDict ，在字符串 s 中增加空格来构建一个句子，使得句子中所有的单词都在词典中。以任意顺序 返回所有这些可
# 能的句子。
#
#  注意：词典中的同一个单词可能在分段中被重复使用多次。
#
#
#
#  示例 1：
#
#
# 输入:s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# 输出:["cats and dog","cat sand dog"]
#
#
#  示例 2：
#
#
# 输入:s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine",
# "pineapple"]
# 输出:["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# 解释: 注意你可以重复使用字典中的单词。
#
#
#  示例 3：
#
#
# 输入:s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# 输出:[]
#
#
#
#
#  提示：
#
#
#
#
#  1 <= s.length <= 20
#  1 <= wordDict.length <= 1000
#  1 <= wordDict[i].length <= 10
#  s 和 wordDict[i] 仅有小写英文字母组成
#  wordDict 中所有字符串都 不同
#
#  Related Topics 字典树 记忆化搜索 哈希表 字符串 动态规划 回溯 👍 585 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # 依据139， 获取每个位置可拆分的点
        n = len(s)
        dp = [False] * (n + 1)
        ans = []
        dp[0] = True
        for i in range(n):
            for j in range(i + 1, n + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True

        def dfs(start, path: List):
            if start >= n:
                ans.append(' '.join(path[:]))
                return
            else:
                for idx in range(start, n):
                    if s[start: idx + 1] in wordDict and dp[i + 1]:
                        path.append(s[start: idx + 1])
                        dfs(idx+1, path)
                        path.pop()

        dfs(0, [])
        return ans


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]))
