class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val

    def set_data(self, new):
        self.val = new

    def get_next(self):
        return self.next

    def set_next(self, nextNode):
        self.next = nextNode


class LinkList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def add_node(self, node):
        if not self.head:
            self.head = node
            self.length += 1
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            # 已遍历到最后的节点
            cur_node.next = node
            self.length += 1

    def insert(self, index, node):
        if index < 0 or index > self.length:
            print('the index is out of range')
            return

        if index == 0:
            node.next = self.head
            self.head = node
            self.length += 1
            return

        cur_p = 0
        cur_node = self.head
        pre_node = None
        while cur_node.next and cur_p < index:
            pre_node = cur_node
            cur_node = cur_node.next
            cur_p += 1

        if cur_p == index:
            node.next = cur_node
            pre_node.next = node
            self.length += 1

    def delete(self, index):
        if self.is_empty():
            print("can not delete an empty link list")
            return

        if index < 0 or index > self.length:
            print('the index is out of range')
            return

        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return

        cur_p = 0
        cur_node = self.head
        pre_node = None
        while cur_node.next and cur_p < index:
            pre_node = cur_node
            cur_node = cur_node.next
            cur_p += 1

        if cur_p == index:
            pre_node.next = cur_node.next
            self.length -= 1
            return

    def empty(self):
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        if self.is_empty() or index < 0 or index >= self.length:
            print('the index is out of range')
            return

        return self.get_node(index)

    def get_node(self, index):
        if self.is_empty() or index < 0 or index >= self.length:
            print('the index is out of range')
            return
        p = 0
        node = self.head
        while node.next and p < index:
            node = node.next
            p += 1
        if p == index:
            return node.val


link_list = LinkList()
link_list.add_node(Node(1))
link_list.add_node(Node(2))
link_list.add_node(Node(3))
