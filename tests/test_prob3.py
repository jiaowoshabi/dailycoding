import pytest
from src.prob3 import Solution, Node

def test_prob3_1():
    s = Solution()
    assert s.serialize(Node('root', Node('left', Node('left.left')), Node('right'))) == ['root', 'left', 'right', 'left.left', None, None, None, None, None]

def test_prob3_2():
    s = Solution()
    assert s.serialize(None) == [] 
    
def test_prob3_3():
    s = Solution()
    assert s.serialize(Node("root")) == ["root", None, None] 

def test_prob3_4():
    s = Solution()
    assert s.deserialize([]) == None

def test_prob3_5():
    s = Solution()
    assert s.deserialize(["root", None, None]).val == "root"

def test_prob3_6():
    s = Solution()
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert s.deserialize(s.serialize(node)).left.left.val == 'left.left'