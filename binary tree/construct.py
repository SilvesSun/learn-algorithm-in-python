# coding:utf-8

"""
在二叉树中有些结点的两棵子树都为空，没有子结点，称为树叶结点，其他的节点称为分支结点。
一个结点的子节点个数称为该结点的度数，二叉树中树叶结点的度数为0，分支结点的度数为1或2
路径中边的条数称为该路径的长度
从树根到树中任一结点的路径长度就是该结点所在的层数
一棵二叉树的高度（深度）是树中结点的最大层数
二叉树是递归结构，python的list的也是递归结构。
基本的二叉树抽象数据类型
ADT BinTree:
    BinTree(self, data, left, right)  # 创建一个新二叉树
    is_empty(self)                    # 判断是否为空
    num_nodes(self)                   # 求二叉树的结点个数
    data(self)                        # 获取二叉树根存储的数据
    left(self)                        # 获得二叉树的左子树
    right(self)                       # 获得二叉树的右子树
    set_left(self, btree)             # 用btree取代原来的左子树
    set_right(self, btree)            # 用btree取代原来的右子树
    traversal(self)                   # 遍历二叉树中个结点数据的迭代器
    forall(self, op)                  # 对二叉树中的各个结点的数据执行操作op
二叉树的常见遍历有：
    先根序列，对称序列，后根序列，宽度优先序列（按层次顺序遍历）
设计：
    空树用None表示
    非空二叉树用包含三个元素的表[d, l, r]表示
    d表示根节点，lr是两颗子树
采用树形结构实现优先队列的一种有效技术称为堆。从结构上看，堆就是结点里存储数据的完全二叉树。堆中的数据要满足一种特殊的堆序，
任一结点里的数据先于或者等于其子结点里的数据。

性质:
1 在二叉树的第 i 层至多有 2^(i －1)个结点。(i>=1)
2 深度为 k 的二叉树至多有 2^(k-1)个结点(k >=1)。
3 对任何一棵二叉树T, 如果其叶结点数为n0, 度为2的结点数为 n2,则n0＝n2＋1
4  具有 n (n>=0) 个结点的完全二叉树的深度为＋1
5  如将一棵有n个结点的完全二叉树自顶向下，同层自左向右连续为结点编号0,1, …, n-1，则有：
       1）若i = 0, 则 i 无双亲,   若i > 0, 则 i 的双亲为」(i -1)/2」
       2）若2*i+1 < n, 则i 的左子女为 2*i+1，若2*i+2 < n, 则 i 的右子女为2*i+2
       3）若结点编号i为偶数，且i != 0,则左兄弟结点i-1.
       4）若结点编号i为奇数，且i != n-1,则右兄弟结点为i+1.
       5）结点i 所在层次为」log2(i+1) 」
"""


class BinaryTree(object):
    def __init__(self, root, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

    # 插入左子树, 构建一个新的节点
    def insert_left(self, node):
        # 如果左子树为空, 直接插入. 否则当前左节点为新的节点的左节点
        if self.left is None:
            self.left = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.left = self.left
            self.left = t

    # 插入右子树同理
    def insert_right(self, node):
        if self.right is None:
            self.right = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.right = self.right
            self.right = t

    # 取得左右子树
    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root