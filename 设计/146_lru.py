# 运用你所掌握的数据结构，设计和实现一个 LRU (最近最少使用) 缓存机制 。
#
#
#
#  实现 LRUCache 类：
#
#
#  LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
#  int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
#  void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上
# 限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
#
#
#
#
#
#
#  进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？
#
#
#
#  示例：
#
#
# 输入
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# 输出
# [null, null, null, 1, null, -1, null, -1, 3, 4]
#
# 解释
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // 缓存是 {1=1}
# lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
# lRUCache.get(1);    // 返回 1
# lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
# lRUCache.get(2);    // 返回 -1 (未找到)
# lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
# lRUCache.get(1);    // 返回 -1 (未找到)
# lRUCache.get(3);    // 返回 3
# lRUCache.get(4);    // 返回 4
#
#
#
#
#  提示：
#
#
#  1 <= capacity <= 3000
#  0 <= key <= 10000
#  0 <= value <= 105
#  最多调用 2 * 105 次 get 和 put
#
#  Related Topics 设计 哈希表 链表 双向链表
#  👍 1627 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.value

    def move_to_head(self, node):
        self.remove(node)
        self.add_to_head(node)

    def remove(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre

    def add_to_head(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.move_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            # 添加至双向链表的头部
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed = self.remove_tail()
                self.cache.pop(removed.key)
                self.size -= 1

    def remove_tail(self):
        node = self.tail.pre
        self.remove(node)
        return node


if __name__ == '__main__':
    cache = LRUCache(2)

    print(cache.put(2, 1), cache.put(2, 2), cache.get(2), cache.put(1, 1), cache.put(4, 1), cache.get(2))