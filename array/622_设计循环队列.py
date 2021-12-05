# 设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”
# 。
#
#  循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环
# 队列，我们能使用这些空间去存储新的值。
#
#  你的实现应该支持如下操作：
#
#
#  MyCircularQueue(k): 构造器，设置队列长度为 k 。
#  Front: 从队首获取元素。如果队列为空，返回 -1 。
#  Rear: 获取队尾元素。如果队列为空，返回 -1 。
#  enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
#  deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
#  isEmpty(): 检查循环队列是否为空。
#  isFull(): 检查循环队列是否已满。
#
#
#
#
#  示例：
#
#  MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
# circularQueue.enQueue(1);  // 返回 true
# circularQueue.enQueue(2);  // 返回 true
# circularQueue.enQueue(3);  // 返回 true
# circularQueue.enQueue(4);  // 返回 false，队列已满
# circularQueue.Rear();  // 返回 3
# circularQueue.isFull();  // 返回 true
# circularQueue.deQueue();  // 返回 true
# circularQueue.enQueue(4);  // 返回 true
# circularQueue.Rear();  // 返回 4
#
#
#
#  提示：
#
#
#  所有的值都在 0 至 1000 的范围内；
#  操作数将在 1 至 1000 的范围内；
#  请不要使用内置的队列库。
#
#  Related Topics 设计 队列 数组 链表
#  👍 236 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class MyCircularQueue:
    """
    对于一个固定大小的数组，任何位置都可以是队首，只要知道队列长度，就可以根据下面公式计算出队尾位置
    tail = (head + count -1) % cap
    cap 数组长度， head tail 分别是队首和队尾
    """

    def __init__(self, k: int):
        self.count = 0
        self.queue = [0] * k
        self.head = 0
        self.cap = k

    def enQueue(self, value: int) -> bool:
        if self.count == self.cap:
            return False
        self.queue[(self.head + self.count - 1) % self.cap] = value
        self.count += 1
        return True


    def deQueue(self) -> bool:
        if self.count == 0:
            return False
        self.head  = (self.head + 1) % self.cap
        self.count -= 1
        return True

    def Front(self) -> int:
        if self.count == 0:
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        # Get the last item from the queue
        if self.count == 0:
            return -1
        return self.queue[(self.head + self.count) % self.cap]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.cap


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# leetcode submit region end(Prohibit modification and deletion)
