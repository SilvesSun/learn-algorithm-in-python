# 给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。
#
#  单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使
# 用。
#
#
#
#  示例 1：
#
#
# 输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f",
# "l","v"]], words = ["oath","pea","eat","rain"]
# 输出：["eat","oath"]
#
#
#  示例 2：
#
#
# 输入：board = [["a","b"],["c","d"]], words = ["abcb"]
# 输出：[]
#
#
#
#
#  提示：
#
#
#  m == board.length
#  n == board[i].length
#  1 <= m, n <= 12
#  board[i][j] 是一个小写英文字母
#  1 <= words.length <= 3 * 10⁴
#  1 <= words[i].length <= 10
#  words[i] 由小写英文字母组成
#  words 中的所有字符串互不相同
#
#  Related Topics 字典树 数组 字符串 回溯 矩阵 👍 628 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
from typing import List

from collections import defaultdict


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.word = ""

    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.children[c]
        cur.is_word = True
        cur.word = word


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        根据题意，我们需要逐个遍历二维网格中的每一个单元格；然后搜索从该单元格出发的所有路径，找到其中对应words 中的单词的路径, 这里用到回溯过程
        遍历过程中, 为了防止单词被重复使用, 将遍历过的字母临时修改为 #, 以避免再次经过该单元格

        剪枝: 如果当前路径是words中的单词, 将其添加到结果集中. 如果是任意单词的前缀, 继续搜索, 反之剪枝
        """
        trie = Trie()
        for word in words:
            trie.insert(word)

        def dfs(now, i1, j1):
            if board[i1][j1] not in now.children:
                return

            ch = board[i1][j1]

            now = now.children[ch]
            if now.word != "":
                ans.add(now.word)

            board[i1][j1] = "#"
            for i2, j2 in [(i1 + 1, j1), (i1 - 1, j1), (i1, j1 + 1), (i1, j1 - 1)]:
                if 0 <= i2 < m and 0 <= j2 < n:
                    dfs(now, i2, j2)
            board[i1][j1] = ch

        ans = set()
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                dfs(trie, i, j)

        return list(ans)


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    print(Solution().findWords([["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
                               words=["oath", "pea", "eat", "rain"]))
