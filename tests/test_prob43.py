from src.prob43 import Solution

def test_prob43_push():
    s = Solution()

    s.push(1)
    assert s.stack == [1]
    assert s.max_curr == [1]

    s.push(4)
    assert s.stack == [1,4]
    assert s.max_curr == [1,4]

    s.push(2)
    assert s.stack == [1,4,2]
    assert s.max_curr == [1,4]

def test_prob43_pop1():
    s = Solution()

    s.push(1)
    assert s.stack == [1]
    assert s.max_curr == [1]

    assert s.pop() == 1
    assert s.stack == []
    assert s.stack == []

def test_prob43_pop2():
    s = Solution()
    s.push(1)
    assert s.stack == [1]
    assert s.max_curr == [1]

    s.push(4)
    assert s.stack == [1,4]
    assert s.max_curr == [1,4]

    s.push(2)
    assert s.stack == [1,4,2]
    assert s.max_curr == [1,4]

    assert s.pop() == 2
    assert s.stack == [1,4]
    assert s.stack == [1,4]

def test_prob43_max():
    s = Solution()
    s.push(1)
    s.push(4)
    s.push(2)
    assert s.max() == 4
