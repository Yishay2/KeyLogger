from xxsubtype import bench


class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.right = None
        self.left = None
        self.height = 1

class AvlTree:

    def __init__(self):
        self.root = None

    def search(self, data: int):
        return self._search(self.root, data)

    def _search(self, root: TreeNode, data: int):
        if not root: return False

        if root.data == data: return True

        elif root.data > data:
            return self._search(root.left, data)
        else:
            return self._search(root.right, data)

    def insert(self, data: int):
        return self._insert(self.root, data)

    def _insert(self, root: TreeNode, data: int):
        if not root:
            return TreeNode(data)

        if root.data > data:
            root.left = self._insert(root.left, data)
        if root.data < data:
            root.right = self._insert(root.right, data)

        self._update_height(root)
        return self._balance_tree(root)

    def delete(self, data):
        return self._delete(self.root, data)

    def _delete(self, root, data):
        pass

    def _get_height(self, node: TreeNode):
        return node.height if node else 0

    def _update_height(self, node: TreeNode):
        if node:
            node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

    def _get_balance(self, node: TreeNode):
        return self._get_height(node.left) - self._get_height(node.right) if node else 0

    def _right_rotate(self, y: TreeNode):
        x = y.left
        t1 = x.right

        x.right = y
        y.left = t1

        return x


    def left_rotate(self, y: TreeNode):
        x = y.right
        t1 = x.left

        x.left = y
        y.right = t1

        return x

    def _balance_tree(self, root):
        if root:
            balance = self._get_balance(root)
            if -1 <= balance <= 1:
                return root

            if balance > 1:
                # we need to implement right rotation and left right rotation
                pass

            if balance < 1:
                # we need to implement left rotation and right left rotation
                pass


def f(x):
    while True:
        yield x + 1


g = f(2)
print(next(g))
print(next(g))
print(next(g))