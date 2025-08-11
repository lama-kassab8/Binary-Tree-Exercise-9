# Binary Tree from Array

This project demonstrates how to build a binary tree from an array representation using two approaches in Python:

- **Iterative method**: Creates all nodes first, then links them based on the array index.
- **Recursive method**: Builds the tree recursively by mapping array indices to nodes.

## How it works

A binary tree can be represented as an array where for any element at index `i`:

- Left child is at index `2*i + 1`
- Right child is at index `2*i + 2`
- Parent is at index `(i - 1) // 2`

Using these formulas, the tree structure can be recreated from the array.

## Code overview

- `Node` class: Represents a tree node with `data`, `left`, and `right` attributes.
- `BinaryTree` class:  
  - `array_to_tree(arr)`: Builds the tree iteratively from the array.
  - `recursive_array_to_tree(arr)`: Builds the tree recursively.

