class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


def levelorder(root):
    if root is None:
        return

    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)



root = Node("CEO")

root.left = Node("Manager1")
root.right = Node("Manager2")

root.left.left = Node("Employee1")
root.left.right = Node("Employee2")

root.right.left = Node("Employee3")
root.right.right = Node("Employee4")


print("Inorder:")
inorder(root)

print("\nPreorder:")
preorder(root)

print("\nPostorder:")
postorder(root)

print("\nLevel Order:")
levelorder(root)