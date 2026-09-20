# Python Trees

## Explanation

A Tree is a non-linear data structure that stores elements in a hierarchical structure.

A **Binary Tree** is a tree in which each node can have at most two children:

* Left child
* Right child

This program creates a Binary Tree and demonstrates three common tree traversals:

* Inorder
* Preorder
* Postorder

## Problem Statement

Write a Python program to create a Binary Tree and perform different tree traversal operations.

## Features

* Creates Binary Tree nodes
* Connects nodes using left and right references
* Performs Inorder traversal
* Performs Preorder traversal
* Performs Postorder traversal

## How It Works

1. A `Node` class is created to store data.
2. Each node can have a left and right child.
3. A sample Binary Tree is constructed.
4. Recursive functions are used for tree traversal.
5. The elements are displayed according to each traversal method.

## Technologies Used

* Python 3

## Data Structure Used

* Binary Tree
* Nodes

## Methods Used

* `__init__()`
* `inorder()`
* `preorder()`
* `postorder()`

## Program Flow

1. Create the root node.
2. Create child nodes.
3. Connect the nodes.
4. Perform Inorder traversal.
5. Perform Preorder traversal.
6. Perform Postorder traversal.
7. Display the results.

## Sample Input

The tree is created using the following values:

```text
        1
       / \
      2   3
     / \
    4   5
```

## Sample Output

```text
Inorder: 4 2 5 1 3
Preorder: 1 2 4 5 3
Postorder: 4 5 2 3 1
```

## Time Complexity

For each traversal:

* O(n)

where `n` is the number of nodes.

## Space Complexity

* O(h)

where `h` is the height of the tree due to recursive calls.

## Key Learning

* Understanding tree data structures
* Understanding Binary Trees
* Creating tree nodes
* Understanding parent-child relationships
* Learning tree traversal techniques
* Using recursion with trees

## File Location

```text
Python-Trees/trees.py
```

## Repository Structure

```text
Python-Trees/
│
├── trees.py
└── README.md
```

## Author

V.Harini
