# 字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 ->
# s2 -> ... -> sk：
#
#
#  每一对相邻的单词只差一个字母。
#  对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。
#  sk == endWord
#
#
#  给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列
# 中的 单词数目 。如果不存在这样的转换序列，返回 0 。
#
#
#  示例 1：
#
#
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot",
# "log","cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
#
#
#  示例 2：
#
#
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot",
# "log"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。
#
#
#
#  提示：
#
#
#  1 <= beginWord.length <= 10
#  endWord.length == beginWord.length
#  1 <= wordList.length <= 5000
#  wordList[i].length == beginWord.length
#  beginWord、endWord 和 wordList[i] 由小写英文字母组成
#  beginWord != endWord
#  wordList 中的所有字符串 互不相同
#
#  Related Topics 广度优先搜索 哈希表 字符串 👍 1021 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import string
from typing import List
from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        s = set(wordList)
        dist = defaultdict(int)
        dist[beginWord] = 1
        queue = deque([beginWord])
        chars = string.ascii_lowercase
        while queue:
            t = queue.popleft()
            r = t
            for i in range(len(r)):
                tmp_list = list(r)
                for c in chars:
                    if tmp_list[i] != c:
                        tmp_list[i] = c
                        tmp_s = ''.join(tmp_list)
                        if tmp_s in s and dist[tmp_s] == 0:
                            dist[tmp_s] = dist[t] + 1
                            print(dist)
                            if tmp_s == endWord:
                                return dist[tmp_s]
                            queue.append(tmp_s)
        return 0


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    print(Solution().ladderLength(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"]))
