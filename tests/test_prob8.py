from src.prob3 import Node
from src.prob3 import Solution as p3
from src.prob8 import Solution as p8

def test_prob8_1():
    s1 = p3()
    tree1 = s1.deserialize(["1", None, None])
    tree2 = s1.deserialize(["1", "1", "1", None, None, None, None])
    # tree3 = s1.deserialize(["1", "1", "1", "0", None, ])

    s2 = p8()
    # assert s2.is_unival(tree1)
    # assert s2.is_unival(tree2)
    # assert not s2.is_unival(tree3)
