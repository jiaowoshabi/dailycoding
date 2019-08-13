from src.prob22 import Solution

def test_prob22_1():
    sentense = "thequickbrownfox"
    voc = {'quick', 'brown', 'the', 'fox'}
    s = Solution()
    assert s.better_solution(voc, sentense) == ['the', 'quick', 'brown', 'fox']

def test_prob22_2():
    sentense = "bedbathandbeyond"
    voc = {'bed', 'bath', 'bedbath', 'and', 'beyond'}
    s = Solution()
    assert (s.better_solution(voc, sentense) == ['bed', 'bath', 'and', 'beyond']) or \
             (s.better_solution(voc, sentense) == ['bedbath', 'and', 'beyond'])

def test_prob22_3():
    sentense = "theremin"
    voc = {'the', 'theremin'}
    s = Solution()
    assert (s.better_solution(voc, sentense) == ['theremin'])