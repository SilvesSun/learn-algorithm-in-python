# 请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。
#
#  实现 LFUCache 类：
#
#
#  LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
#  int get(int key) - 如果键 key 存在于缓存中，则获取键的值，否则返回 -1 。
#  void put(int key, int value) - 如果键 key 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量
# capacity 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最近最久未使用 的键。
#
#
#  为了确定最不常使用的键，可以为缓存中的每个键维护一个 使用计数器 。使用计数最小的键是最久未使用的键。
#
#  当一个键首次插入到缓存中时，它的使用计数器被设置为 1 (由于 put 操作)。对缓存中的键执行 get 或 put 操作，使用计数器的值将会递增。
#
#  函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。
#
#
#
#  示例：
#
#
# 输入：
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get",
# "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# 输出：
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
#
# 解释：
# // cnt(x) = 键 x 的使用计数
# // cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // 返回 1
#                  // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
#                  // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // 返回 -1（未找到）
# lfu.get(3);      // 返回 3
#                  // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
#                  // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // 返回 -1（未找到）
# lfu.get(3);      // 返回 3
#                  // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // 返回 4
#                  // cache=[3,4], cnt(4)=2, cnt(3)=3
#
#
#
#  提示：
#
#
#  0 <= capacity <= 10⁴
#  0 <= key <= 10⁵
#  0 <= value <= 10⁹
#  最多调用 2 * 10⁵ 次 get 和 put 方法
#
#  Related Topics 设计 哈希表 链表 双向链表 👍 508 👎 0

"""
LFU 需要用两个哈希表加N个双链表实现。
第一个哈希表的key是输入的key， value 是Node对象， 记录key， value， frequency。
第二个哈希表为频率哈希表
"""


# leetcode submit region begin(Prohibit modification and deletion)
class Node(object):
    """
    双链表中的链表节点对象
    """

    def __init__(self, key=None, value=None, freq=0):
        """
        Args:
            key:对应输入的key
            value:对应输入的value
            freq:被访问的频率
            pre:指向前一个节点的指针
            next:指向后一个节点的指针
        """
        self.key = key
        self.value = value
        self.freq = freq
        self.pre = None
        self.next = None


class LinkedList(object):
    """
    自定义的双向链表
    """

    def __init__(self):
        """
        Args:
            __head:双向链表的头结点
            __tail:双向链表的尾节点
        """
        self.__head = Node()
        self.__tail = Node()
        self.__head.next = self.__tail
        self.__tail.pre = self.__head

    def insertFirst(self, node):
        """
        将指定的节点插入到链表的第一个位置
        Args:
            node:将要插入的节点
        """
        node.next = self.__head.next
        self.__head.next.pre = node
        self.__head.next = node
        node.pre = self.__head

    def delete(self, node):
        """
        从链表中删除指定的节点
        Args:
            node:将要删除的节点
        """
        if self.__head.next == self.__tail:
            return
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = None
        node.pre = None

    def get_last(self):
        """
        从链表中获取最后一个节点
        Returns:
            双向链表中的最后一个节点，如果是空链表则返回None
        """
        if self.__head.next == self.__tail:
            return None
        return self.__tail.pre

    def is_empty(self):
        """
        判断链表是否为空，除了head和tail没有其他节点即为空链表
        Returns:
            链表不空返回True，否则返回False
        """
        return self.__head.next == self.__tail


class LFUCache(object):
    """
    自定义的LFU缓存
    """

    def __init__(self, capacity):
        """
        Args:
            __capacity:缓存的最大容量
            __keyMap: key->Node 这种结构的字典
            __freqMap:freq->LinkedList 这种结构的字典
            __minFreq:记录缓存中最低频率
        """
        self.__capacity = capacity
        self.__keyMap = dict()
        self.__freqMap = dict()
        self.__minFreq = 0

    def get(self, key):
        """
        获取一个元素，如果key不存在则返回-1，否则返回对应的value
        同时更新被访问元素的频率
        Args:
            key:要查找的关键字
        Returns:
            如果没找到则返回-1，否则返回对应的value
        """
        if key not in self.__keyMap:
            return -1
        node = self.__keyMap[key]
        self.__increment(node)
        return node.value

    def put(self, key, value):
        """
        插入指定的key和value，如果key存在则更新value，同时更新频率
        如果key不存并且缓存满了，则删除频率最低的元素，并插入新元素
        否则，直接插入新元素
        Args:
            key:要插入的关键字
            value:要插入的值
        """
        if key in self.__keyMap:
            node = self.__keyMap[key]
            node.value = value
            self.__increment(node)
        else:
            if self.__capacity == 0:
                return
            if len(self.__keyMap) == self.__capacity:
                self.__remove_min_freq_element()
            node = Node(key, value, 1)
            self.__increment(node, True)
            self.__keyMap[key] = node

    def __increment(self, node, is_new_node=False):
        """
        更新节点的访问频率
        Args:
            node:要更新的节点
            is_new_node:是否是新节点，新插入的节点和非新插入节点更新逻辑不同
        """
        if is_new_node:
            self.__minFreq = 1
            self.__set_default_linked_list(node)
        else:
            self.__delete_node(node)
            node.freq += 1
            self.__set_default_linked_list(node)
            if self.__minFreq not in self.__freqMap:
                self.__minFreq += 1

    def __set_default_linked_list(self, node):
        """
        根据节点的频率，插入到对应的LinkedList中，如果LinkedList不存在则创建
        Args:
            node:将要插入到LinkedList的节点
        """
        if node.freq not in self.__freqMap:
            self.__freqMap[node.freq] = LinkedList()
        linkedList = self.__freqMap[node.freq]
        linkedList.insertFirst(node)

    def __delete_node(self, node):
        """
        删除指定的节点，如果节点删除后，对应的双链表为空，则从__freqMap中删除这个链表
        Args:
            node:将要删除的节点
        """
        if node.freq not in self.__freqMap:
            return
        linked_list = self.__freqMap[node.freq]
        freq = node.freq
        linked_list.delete(node)
        if linked_list.is_empty():
            del self.__freqMap[freq]

    def __remove_min_freq_element(self):
        """
        删除频率最低的元素，从__freqMap和__keyMap中都要删除这个节点，如果节点删除后对应的链表为空，则要从__freqMap中删除这个链表
        """
        linked_list = self.__freqMap[self.__minFreq]
        node = linked_list.get_last()
        linked_list.delete(node)
        del self.__keyMap[node.key]
        if linked_list.is_empty():
            del self.__freqMap[node.freq]

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
