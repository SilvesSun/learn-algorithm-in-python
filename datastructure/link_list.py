class ListNode(object):
    def __init__(self, val, node_next=None):
        self.val = val
        self.p_next = node_next

    def __repr__(self):
        return f'node: value {self.val}, p_next -> {self.p_next}'


class LinkList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def is_empty(self):
        return self.length == 0

    def append(self, val: any):
        """
        链表尾插入元素
        :param val:
        :return:
        """
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.length += 1
            return

        cur = self.head
        while cur.p_next:
            cur = cur.p_next
        cur.p_next = node
        self.length += 1

    def insert(self, index, val):
        if self.is_empty():
            print("empty chain")
            return
        insert_node = ListNode(val)
        if index == 0:
            insert_node.p_next = self.head
            self.head = insert_node
            self.length += 1

        p = 0
        cur_node = self.head
        pre_node = self.head
        while cur_node.p_next and p < index:
            pre_node = cur_node
            cur_node = cur_node.p_next
            p += 1
        if p == index:
            insert_node.p_next = cur_node
            pre_node.p_next = insert_node
            self.length += 1

    def get_index(self, val):
        p = 0
        if self.is_empty():
            print('empty chain')
            return
        node = self.head
        while node:
            if node.val == val:
                return p
            node = node.p_next
            p += 1
        if p == self.length:
            print(f'{val} not found')
            return

    def delete(self, index):
        if self.is_empty():
            return

        if index < 0 or index >= self.length:
            print('index out of range')
            return

        if index == 0:
            self.head = self.head.p_next
            self.length -= 1

        p = 0
        cur_node = self.head
        pre_node = self.head

        while cur_node.p_next and p < index:
            pre_node = cur_node
            cur_node = cur_node.p_next
            p += 1

        if p == index:  # find the node to delete
            pre_node.p_next = cur_node.p_next
            self.length -= 1

    def update(self, index, val):
        if self.is_empty():
            return

        if index < 0 or index >= self.length:
            print('index out of range')
            return

        p = 0
        cur_node = self.head
        while cur_node.p_next and p < index:
            cur_node = cur_node.p_next
            p += 1

        if p == index:
            cur_node.val = val

    def get_val(self, index):
        if self.is_empty():
            return

        if index < 0 or index >= self.length:
            print('index out of range')
            return

        p = 0
        cur_node = self.head
        while cur_node.p_next and p < index:
            cur_node = cur_node.p_next
            p += 1

        return cur_node.val

    def clear(self):
        self.head = None
        self.length = 0

    def to_list(self):
        if self.is_empty():
            return

        nodes = []
        node = self.head
        while node:
            nodes.append(node.val)
            node = node.p_next
        return nodes

    def __repr__(self):
        if self.is_empty():
            return 'empty chain'
        return str(self.to_list())


if __name__ == '__main__':
    chain = LinkList()
    for i in range(10):
        chain.append(i)
    chain.delete(5)

