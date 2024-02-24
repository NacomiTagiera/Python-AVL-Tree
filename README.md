## AVL Tree Implementation in Python

This repository contains a Python implementation of an AVL tree. AVL tree is a **self-balancing Binary Search Tree (BST)** where the difference between heights of left and right subtrees cannot be more than one for all nodes.
<p align="center">
  <img src="https://github.com/NacomiTagiera/Python-AVL-Tree/assets/106376178/0f13423b-ff57-437c-95b7-e9f59b22d43e" />
</p>

### Features

The code provides the following operations:
1. **Insertion**: Add a node to the tree.
2. **Deletion**: Remove a node from the tree.
3. **Pre-order Traversal**: Traverse the AVL tree in pre-order manner and save the result to a file.
4. **Display**: Print the AVL tree structure on the screen.
5. **Search**: Search for an element in the tree.
6. **Random Number Generation**: Generate random numbers and add them to the tree.
7. **Load from File**: Load tree nodes from a file and construct the AVL tree.
8. **Delete Tree**: Delete all nodes from the tree.

### Usage

The main function of the program is `menu(tree, root)`, which provides an interactive menu for performing the above operations.

```python
myTree = AvlTree()
root = None
root = myTree.insert_from_file(root)
menu(myTree, root)
```

### File Structure

The `tree.txt` file is used for storing and loading tree nodes. The `insert_from_file(root)` function reads this file and inserts each number into the AVL tree. The `pre_order(root)` function writes the pre-order traversal of the tree to this file.

#### Note

<small>This is a basic implementation and does not handle all edge cases. Please use it as a starting point and modify according to your needs.</small>
