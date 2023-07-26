# 链表节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 链表类
class LinkedList:
    def __init__(self):
        self.head = None

    def addAtHead(self, val: int) -> None:
        self.head = ListNode(val, self.head)

    def addAtTail(self, val: int) -> None:
        if not self.head:
            self.head = ListNode(val)
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = ListNode(val)

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
                if not cur:
                    return
            if not cur.next:
                return
            cur.next = cur.next.next

    def get(self, index: int) -> int:
        if not self.head:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
            if not cur:
                return -1
        return cur.val

    # 创建一个链表


# 创建一个链表
l = LinkedList()

# 向链表头部添加节点
l.addAtHead(1)

# 向链表尾部添加节点
l.addAtTail(2)

# 获取链表中第一个节点的值
print(l.get(0))  # 输出 1

# 获取链表中第二个节点的值
print(l.get(1))  # 输出 2

# 删除链表中第二个节点
l.deleteAtIndex(1)

# 获取链表中第二个节点的值
print(l.get(1))  # 输出 -1，因为第二个节点已经被删除了
