# implements an array with an array

class Queue:
    def __init__(self):
        self.arr = []

    def is_empty(self):
        return len(self.arr) == 0

    def enqueue(self, data):
        self.arr.append(data)

    def dequeue(self):
        self.arr.pop(0)

    def head(self):
        if self.is_empty():
            print("You don't have any elements in the array!")
        else:
            return self.arr[0]


# implements an array with linked list with tail
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"data: {self.data}"

class LinkedList:

    def __init__(self):
        self._head = None
        self.tail = None

    def is_empty(self):
        return self._head is None

    def head(self):
        if self._head is None:
            print("You don't have any elements in the queue!")
            return

        return self._head


    def enqueue(self, node):
        if self.is_empty():
           self._head = node
           self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def enqueue_to_the_right_place(self, node):
        if self.is_empty():
            self._head = node
            self.tail = node

        current = self._head
        prev = current
        while True:
            if current.data > node.data:
                current = current.next
                prev = current
            else:
                break

        if prev == current:
            self.head = current

        prev.next = node
        node.next = current

    def dequeue(self):
        if self.is_empty():
            print("You don't have any nodes in the list!")
            return

        data = self._head
        if self._head == self.tail:
            self._head = self.tail = None
            return data
        self._head = self._head.next
        return data

l1 = LinkedList()
l1.enqueue_to_the_right_place(Node(1))
l1.enqueue_to_the_right_place(Node(2))
l1.enqueue_to_the_right_place(Node(3))
l1.enqueue_to_the_right_place(Node(90))
l1.enqueue_to_the_right_place(Node(70))

for i in range(5):
    print(l1.dequeue())
l1.enqueue(Node(4))


#implement a queue in array with constant size

class Queue:

    def __init__(self, size):
        self.arr = [None] * size
        self._head = 0
        self.tail = -1

    def is_empty(self):
        return self.arr[self._head] is None

    def __repr__(self):
        return f"arr: {self.arr}"

    def enqueue(self, x):

        self.tail = (self.tail + 1) % len(self.arr)
        if self.arr[self.tail] is None:
            self.arr[self.tail] = x
        else:
            # create a new array
            new_arr = [None] * (len(self.arr) * 2)
            old_size = len(self.arr)
            for i in range(old_size):
                new_arr[i] = self.dequeue()
            self.arr = new_arr
            self._head = 0
            self.tail = old_size
            self.enqueue(x)

    def dequeue(self):
        if self.arr[self._head] is None:
            print("You don't have any items in the queue!")
            return None

        data = self.arr[self._head]
        self.arr[self._head] = None
        self._head = (self._head + 1) % len(self.arr)
        return data

    def head(self):
        return self.arr[self._head]

#
# q = Queue(3)
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# q.enqueue(5)
# q.enqueue(6)
# q.enqueue(7)
# print(q)