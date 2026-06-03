from binary_tree import BinaryTree
from typing import Union

def paths_sum(tree: Union[BinaryTree, None]) -> int:
    """
    Computes the sum of all the *path amounts* for each root-to-leaf path in the tree.

    Args:
        tree: a binary tree with integer values

    Returns: The sum of all the *path amounts* for each root-to-leaf path in the tree.
    """
    sum = rec(tree, 0)
    return sum

def rec(tree: Union[BinaryTree, None], sum: int) -> int:
    if tree is None:
        return 0
    elif tree.left == None and tree.right == None:
        return sum * tree.value
    elif tree.left == None:
        return rec(tree.right, sum+1)
    elif tree.right == None:
        return rec(tree.left, sum+1)
    else:
        return rec(tree.left, sum+1) + rec(tree.right, sum+1)

# The functions below are for testing purposes only and should not be called
# from the paths_sum() function

def mk_node(val: int,
            left: Union[BinaryTree, None],
            right: Union[BinaryTree, None]) -> BinaryTree:
    """
    Create a binary tree node, given the integer value,
    left child, and right child.

    Args:
        val: the integer value of the new node 
        left: the left branch of the new node 
        right: the right branch of the new node 

    Returns: A new binary tree node with the given value, left child, and right child.  
    """
    t = BinaryTree(val)
    t.left = left
    t.right = right
    return t


def mk_sample_tree() -> BinaryTree:
    '''
    Generates sample tree from the problem statement.

    Args: None 
 
    Returns: the sample tree from the problem statement.
    '''
    return mk_node(10,
               mk_node(5,
                   mk_node(7, None,None),
                   mk_node(4, None,None)),
               mk_node(8,
                   mk_node(6,None, mk_node(2,None,None)),
                   None))
