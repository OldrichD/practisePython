# exercise to practise binary tree

import turtle


# Node with value, left and right descendants
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# class with staticmethod for recursive generating binary tree for depth of n
class BinaryTreeBuilder:
    @staticmethod
    def binary_tree_generator(n, current_level=1, current_value=1):
        if current_level > n:
            return None
        node = Node(current_value)
        node.left = BinaryTreeBuilder.binary_tree_generator(n, current_level + 1, current_value * 2)
        node.right = BinaryTreeBuilder.binary_tree_generator(n, current_level + 1, current_value * 2 + 1)
        return node


# # method for recursive print binary tree
# def print_tree_inorder(node):
#     if node:
#         print_tree_inorder(node.left)
#         print(node.value, end=" ")
#         print_tree_inorder(node.right)


# class for graphical representation of binary tree via turtle library
class BinaryTreeDrawer:
    def __init__(self):
        self.screen = turtle.Screen()
        self.turtle = turtle.Turtle()
        self.turtle.speed(1)

    def draw_tree(self, root, x=0, y=0, space=50):
        if root:
            self.turtle.penup()
            self.turtle.goto(x, y)
            self.turtle.pendown()
            self.turtle.circle(20, extent=360)
            self.turtle.penup()
            self.turtle.goto(x, y + 10)
            self.turtle.pendown()
            self.turtle.write(str(root.value), align="center", font=("Arial", 12, "normal"))
            self.draw_tree(root.left, x - int(space), y - 60, int(space / 2))
            self.draw_tree(root.right, x + int(space), y - 60, int(space / 2))


# example of use class Node and BinaryTreeBuilder
binary_tree_depth = 3
tree_root = BinaryTreeBuilder.binary_tree_generator(binary_tree_depth)

# # print binary tree with print_tree_inorded method
# print("Inorder walk trough generated binary tree:")
# print_tree_inorder(root)

# example of graphical representation of binary tree with BinaryTreeDrawer via turtle library
drawer = BinaryTreeDrawer()
drawer.draw_tree(tree_root)
turtle.done()
