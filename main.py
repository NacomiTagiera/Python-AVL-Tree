import random


class TreeNode(object):
  def __init__(self, key):
    self.key = key
    self.left = None
    self.right = None
    self.height = 1


class AvlTree(object):
  def insert_node(self, root, key):
    if not root:
      return TreeNode(key)
    elif key < root.key:
      root.left = self.insert_node(root.left, key)
    elif key > root.key:
      root.right = self.insert_node(root.right, key)
    else:
      print('No duplicates can be inserted!\n')

    root, balanceFactor = self.update_balance(root)

    if balanceFactor > 1:
      if key < root.left.key:
        return self.right_rotate(root)      
      root.left = self.left_rotate(root.left)
      return self.right_rotate(root)

    if balanceFactor < -1:
      if key > root.right.key:
        return self.left_rotate(root)      
      root.right = self.right_rotate(root.right)
      return self.left_rotate(root)

    return root

  def delete_node(self, root, key):
    if not root:
      return root
    elif key < root.key:
      root.left = self.delete_node(root.left, key)
    elif key > root.key:
      root.right = self.delete_node(root.right, key)
    else:
      if root.left is None:
        temp = root.right
        root = None
        return temp
      elif root.right is None:
        temp = root.left
        root = None
        return temp
      temp = self.get_min_value_node(root.right)
      root.key = temp.key
      root.right = self.delete_node(root.right, temp.key)
    if root is None:
      return root

    root, balanceFactor = self.update_balance(root)

    if balanceFactor > 1:
      if self.get_balance(root.left) >= 0:
        return self.right_rotate(root)      
      root.left = self.left_rotate(root.left)
      return self.right_rotate(root)

    if balanceFactor < -1:
      if self.get_balance(root.right) <= 0:
        return self.left_rotate(root)
      root.right = self.right_rotate(root.right)
      return self.left_rotate(root)
    return root

  def update_balance(self, root):
    if not root:
      return root

    root.height = 1 + max(self.get_height(root.left), self.get_height(
        root.right))
    balanceFactor = self.get_balance(root)

    return root, balanceFactor

  def left_rotate(self, z):
    y = z.right
    T2 = y.left
    y.left = z
    z.right = T2
    z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
    y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
    return y

  def right_rotate(self, z):
    y = z.left
    T3 = y.right
    y.right = z
    z.left = T3
    z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
    y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
    return y

  def get_height(self, root):
    if not root:
      return 0
    return root.height

  def get_balance(self, root):
    if not root:
      return 0
    return self.get_height(root.left) - self.get_height(root.right)

  def get_min_value_node(self, root):
    if root is None or root.left is None:
      return root
    return self.get_min_value_node(root.left)

  def pre_order(self, root):
    with open('tree.txt', 'w') as f:
      self._preorder_helper(root, f)

  def _preorder_helper(self, node, file):
    if node:
      print(node.key, end=" ")
      file.write(str(node.key) + '\n')
      self._preorder_helper(node.left, file)
      self._preorder_helper(node.right, file)

  def search(self, root, key):
    if root is None:
      return False

    if key == root.key:
      return True
    elif key < root.key:
      return self.search(root.left, key)
    
    return self.search(root.right, key)

  def _print_helper(self, node, prefix="", isLeft=True):
    if node is not None:
      self._print_helper(node.right, prefix + ("│   " if isLeft else "    "),
                       False)
      print(prefix + ("└── " if isLeft else "┌── ") + str(node.key))
      self._print_helper(node.left, prefix + ("    " if isLeft else "│   "),
                       True)

  def insert_random_numbers(self, root, n):
    with open('tree.txt', 'w') as f:
      for _ in range(n):
        key = random.randint(1, 10000)
        f.write(str(key) + '\n')
        root = self.insert_node(root, key)
    return root

  def insert_from_file(self, root):
    with open('tree.txt', 'r') as f:
      for line in f:
        key = int(line.strip())
        root = self.insert_node(root, key)
    return root

  def delete_tree(self, root):
    while root is not None:
      root = self.delete_node(root, root.key)
    return root


def menu(tree, root):
  while True:
    print("\n1. Add a number")
    print("2. Delete a node")
    print("3. Print pre-order traversal and save to a file")
    print("4. Display on the screen")
    print("5. Search for an element")
    print("6. Generate random numbers and add to the tree")
    print("7. Load tree from a file")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
      key = int(input("Number: "))
      root = tree.insert_node(root, key)
    elif choice == '2':
      key = int(input("Which node to delete?: "))
      root = tree.delete_node(root, key)
    elif choice == '3':
      print("Pre-order: ")
      tree.pre_order(root)
    elif choice == '4':
      tree._print_helper(root)
    elif choice == '5':
      key = int(input("Element to search for: "))
      if tree.search(root, key):
        print("The number is in the tree")
      else:
        print("The number is not in the tree")
    elif choice == '6':
      n = int(input("How many numbers to generate?: "))
      root = tree.insert_random_numbers(root, n)
    elif choice == '7':
      root = tree.delete_tree(root)
      root = tree.insert_from_file(root)
    else:
      break


myTree = AvlTree()
root = None
root = myTree.insert_from_file(root)
menu(myTree, root)
