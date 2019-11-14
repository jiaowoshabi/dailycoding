from src.prob146 import Solution
from src.utils import TreeNode, deserialize, drawtree

def test_prob146_1():
    s = Solution()
    # root = deserialize('[0,1,0,null,null,1,0,0,0,null,null]')
    # new = s.solution(root)
    # drawtree(new)

    root = deserialize('[0,1,0,null,null,0,0,null,null,null,null]')
    new = s.solution(root)
    drawtree(new)