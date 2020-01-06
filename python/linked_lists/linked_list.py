class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def get_data(self, ):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def get_next(self, ):
        return self.next

    def set_next(self, new_next_node):
        self.next = new_next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = self.head

    @classmethod
    def from_list(cls, datas: list = []):
        ll = LinkedList()
        for d in datas:
            ll.insert(d)
        return ll

    def to_list(self):
        cur_node = self.head
        result = []
        while cur_node:
            result.append(cur_node.data)
            cur_node = cur_node.next
        return result

    def unshift(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def shift(self):
        re_node = self.head
        self.head = re_node.next()
        return re_node

    def insert(self, data):
        """simplified to insert at end only"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.head.set_next(self.tail)
        else:
            self.tail.set_next(new_node)
            self.tail = new_node


def create_linked_list(data: list = []) -> LinkedList:
    ll = LinkedList()
    for d in data:
        ll.insert(d)
    return ll


def print_list(ll: LinkedList):
    cur_node = ll.head
    result = []
    while cur_node:
        result.append(cur_node.data)
        cur_node = cur_node.next
    print(result)


if __name__ == "__main__":
    ll = LinkedList.from_list([1, 2, 3])
    print_list(ll)
    print(ll.to_list())
