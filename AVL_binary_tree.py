# implementation of AVL binary tree exercise

# classical Node binary tree class with parameter height which represent leaf-root distance
class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


#  class consists from methods for handling with AVL binary tree
class AVLTree:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def get_height(self, node):
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    def balance_node(self, root):

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return y

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return Node(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        elif key > root.key:
            root.right = self._insert(root.right, key)
        else:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        return self.balance_node(root)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self._delete(root.left, key)
        elif key > root.key:
            root.right = self._delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self._get_min_value_node(root.right)
            if temp:
                root.key = temp.key
                root.right = self._delete(root.right, temp.key)
            else:
                return None  # Opraveno z return root.right

        # Aktualizace výšky a vyvážení uzlu
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        return self.balance_node(root)

    def _get_min_value_node(self, root):
        while root and root.left:
            root = root.left
        return root

    def print_tree(self, root, level=0, prefix="Root: "):
        if root:
            print(" " * (level * 4) + prefix + str(root.key) + ", height:" + str(root.height))
            if root.left or root.right:
                self.print_tree(root.left, level + 1, "L--- ")
                self.print_tree(root.right, level + 1, "R--- ")


# place of usage
if __name__ == "__main__":
    avl_tree = AVLTree()

    while True:
        try:
            new_key = int(input("Insert or delete element (type '0' to exit, and use '-' to delete element):"))
            if new_key == 0:
                break
            elif new_key > 0:
                root = avl_tree.insert(new_key)
            elif new_key < 0:
                root = avl_tree.delete(abs(new_key))
            else:
                pass

            avl_tree.print_tree(avl_tree.get_root())
        except ValueError as ve:
            print(f"Error: {ve}")
            pass
