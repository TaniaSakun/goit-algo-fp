class LinkedList:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = self.Node(data)
        new_node.next, self.head = self.head, new_node

    def insert_at_end(self, data):
        new_node = self.Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_from(self, data_list):
        for data in data_list:
            self.insert_at_end(data)
        return self

    def search_node(self, data: int):
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def delete_node(self, data: int):
        cur = self.head
        if cur and cur.data == data:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != data:
            prev, cur = cur, cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def reverse_inplace(self):
        if self.head is None:
            return
        new_ll = self.head
        old_ll = new_ll.next
        new_ll.next = None

        while old_ll:
            cur = old_ll
            old_ll = old_ll.next
            cur.next = new_ll
            new_ll = cur
        self.head = new_ll

    def reverse(self):
        ll_new = LinkedList()
        cur = self.head
        while cur:
            ll_new.insert_at_beginning(cur.data)
            cur = cur.next
        return ll_new

    def sort(self):
        if self.head is None:
            return self
        tmp_ll = self.head.next
        self.head.next = None
        while tmp_ll:
            node = tmp_ll
            tmp_ll = tmp_ll.next
            if self.head.data >= node.data:
                node.next, self.head = self.head, node
            else:
                prev = self.head
                cur = self.head.next
                while cur and (cur.data < node.data):
                    prev, cur = cur, cur.next
                prev.next, node.next = node, cur
        return self

    def merge_sorted(self, other_sorted_ll):
        if not isinstance(other_sorted_ll, LinkedList) or other_sorted_ll.head is None:
            return self
        if self.head is None:
            self.head = other_sorted_ll.head
            return self

        cur2 = other_sorted_ll.head
        while cur2 and (self.head.data > cur2.data):
            t = self.head
            self.head, cur2 = cur2, cur2.next
            self.head.next = t
        prev, cur1 = self.head, self.head.next
        while cur1 and cur2:
            if cur1.data > cur2.data:
                t, cur2 = cur2, cur2.next
                t.next = cur1
                prev.next = t
            else:
                cur1 = cur1.next
            prev = prev.next
        if cur2:
            prev.next = cur2
        return self

    def __str__(self):
        l = list()
        current = self.head
        while current:
            l.append(current.data)
            current = current.next
        return str(l)


def list_task():
    linked_list = LinkedList()
    linked_list.insert_from([2, 3, 3, 1, 2, 3, 4])
    print(f"Current Linked List:            {linked_list}")
    print(f"Sorted Linked List (inplace):   {linked_list.sort()}")
    print(f"Reversed Linked List (new Linked List):  {linked_list.reverse()}")
    print(f"Reversed Linked List (inplace): {linked_list.reverse_inplace()}")
    print(f"Sorted Linked List (inplace):   {linked_list.sort()}")

    linked_list2 = LinkedList().insert_from([5, 0, 1, 2]).sort()
    print(f"Second Linked List (sorted):    {linked_list2}")
    linked_list.merge_sorted(linked_list2)
    print(f"Merge sorted Linked List:       {linked_list}")
