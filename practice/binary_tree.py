
"""
Tree implementation for the Path Sums problem.

**DO NOT** modify this file. Your answer should be placed in the paths_sum.py file.
"""

from typing import Union


class BinaryTree:
    """
    Class for representing binary trees.

    Public attributes:
        value: the value associated with this node represented as an integer
        left: the left child of the node (will be None, if the
            node does not have a left child)
        right: the right child of the node (will be None, if the
            node does not have a right child)

    Public methods: (see below)
    """

    def __init__(self, value: int) -> None:
        """
        Constructor for BinaryTree class.

        Arguments:
            value: the value associated with this node represented as an integer

        Returns:
            None
        """
        self.value = value
        self.left: Union[BinaryTree, None] = None
        self.right: Union[BinaryTree, None] = None