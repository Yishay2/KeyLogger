#"Yishay Doron Cohen"

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, root, data):
        if root is None:
            return False
        if root.data == data:
            return True
        if root.data > data:
            return self._search(root.left, data)
        else:
            return self._search(root.right, data)

    def _insert(self, root, data):
        if root is None:
            return TreeNode(data)
        if root.data > data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)

        return root

    def in_order(self):
        self._in_order(self.root)
        print()

    def _in_order(self, root):
        if root:
            self._in_order(root.left)
            print(root.data, end=" ")
            self._in_order(root.right)

    def pre_order(self):
        self._pre_order(self.root)

    def _pre_order(self, root):
        print(root.data)
        self._pre_order(root.left)
        self._pre_order(root.right)

    def get_num_of_nodes(self):
        return self._get_num_of_nodes(self.root)

    def _get_num_of_nodes(self, root):
        if root:
            return self._get_num_of_nodes(root.left) + self._get_num_of_nodes(root.right) + 1
        return 0

    def get_num_of_leaves(self):
        return self._get_num_of_leaves(self.root)

    def _get_num_of_leaves(self, root):
        if root:
                if root.left is None and root.right is None:
                    return 1
                return self._get_num_of_leaves(root.left) + self._get_num_of_leaves(root.right)
        return 0

    def get_height(self):
        return self._get_height(self.root)

    def _get_height(self, root):
        if root:
            return max(self._get_height(root.right), self._get_height(root.left)) + 1
        return 0

    def check_full(self):
        return self._check_full(self.root)

    def _check_full(self, root):
        if root:
            if root.left is None and root.right is None:
                return True

            if not (root.left and root.right):
                 return False

            return self._check_full(root.right) and self._check_full(root.left)

        return True

    def is_balanced(self):
        return self._is_balanced_tree(self.root)

    def _is_balanced_tree(self, root):
        if root is None:
            return True
        if abs(self._get_height(root.left) - self._get_height(root.right)) > 1:
            return False
        return self._is_balanced_tree(root.left) and self._is_balanced_tree(root.right)

    def delete_node(self, data):
        self.root = self._delete_node(self.root, data)

    def _delete_node(self, root, data):
        if not root:
            return None

        elif root.data > data:
            root.left = self._delete_node(root.left, data)
        elif root.data < data:
            root.right = self._delete_node(root.right, data)

        else:
            # if there is no any children
            if root.left is None and root.right is None:
                return None

            # if there is only one child
            if root.left is None or root.right is None:
                if root.left:
                    return root.left
                else:
                    return root.right

            # if there are two children
            else:
                successor = self.get_successor(root.right)
                root.data, successor.data = successor.data, root.data
                root.right = self._delete_node(root.right, data)

        return root

    def get_successor(self, root):
        if root.left:
            return self.get_successor(root.left)
        return root

    def print_tree_by_level(self):
        self._print_tree_by_level()

    def _print_tree_by_level(self):
        queue = [self.root]
        while queue:
            level = len(queue)

            for i in range(level):
                current = queue.pop(0)

                print(current.data, end=" ")
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            print()

tree = Tree()
data_to_insert = [80, 70, 90, 60, 75, 85, 100]

for data in data_to_insert:
    tree.insert(data)


def get_tree(root, level):
    return _get_tree(root, level)

def _get_tree(root, level):

    if not root:
        return 0

    if level == 0:
        return root.data

    return _get_tree(root.left, level - 1) + _get_tree(root.right, level - 1)


def sum_path(root, target):
    return _sum_path(root, target, 0)

def _sum_path(root, target, sum1):
    if not root:
        return sum1 == target
    return _sum_path(root.left, target, sum1 + root.data) or _sum_path(root.right, target, sum1 + root.data)


def print_paths(tree):
    _print_paths(tree.root, "")

def _print_paths(root, my_str):
    if root:
        if root.left is None and root.right is None:
            my_str += str(root.data)  + "t"
            print(" -> ".join([node for node in my_str.split("t") if node != ""]))
            return

        _print_paths(root.left, my_str + str(root.data) + "t")
        _print_paths(root.right, my_str + str(root.data) + "t")


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        print("Linked list: ")
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next

def sorted_linked_list_from_tree(tree):
    return _sorted_linked_list_from_tree(tree.root, LinkedList())

def _sorted_linked_list_from_tree(root, linked_list:LinkedList):
    if not root:
        return

    _sorted_linked_list_from_tree(root.left, linked_list)
    if not linked_list.head:
        linked_list.head = Node(root.data)
        linked_list.tail = linked_list.head
    else:
        linked_list.tail.next = Node(root.data)
        linked_list.tail = linked_list.tail.next

    _sorted_linked_list_from_tree(root.right, linked_list)

    return linked_list


def make_a_balanced_tree(arr):
    tree = Tree()
    tree.root = _make_a_balanced_tree(arr)
    return tree

def _make_a_balanced_tree(sorted_list):
    if not sorted_list:
        return None

    mid = len(sorted_list) // 2
    root = TreeNode(sorted_list[mid])
    root.left = _make_a_balanced_tree(sorted_list[:mid])
    root.right = _make_a_balanced_tree(sorted_list[mid + 1:])
    return root


def return_balanced_tree(tree):
    arr = return_arr(tree.root)
    return make_a_balanced_tree(arr)

def return_arr(root):

    if not root:
        return []

    return return_arr(root.left) + [root.data] + return_arr(root.right)

avl_tree = return_balanced_tree(tree)
avl_tree.print_tree_by_level()