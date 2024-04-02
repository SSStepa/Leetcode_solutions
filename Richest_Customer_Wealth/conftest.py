import pytest

values = [
    {"input": [[1, 2, 3], [3, 2, 1]], "output": 6},
    {"input": [[1, 5], [7, 3], [3, 5]], "output": 10},
    {"input": [[2, 8, 7], [7, 1, 3], [1, 9, 5]], "output": 17},
]


@pytest.fixture
def testcase_1():
    return {"input": [[1, 2, 3], [3, 2, 1]], "output": 6}


@pytest.fixture
def testcase_2():
    return {"input": [[1, 5], [7, 3], [3, 5]], "output": 10}


@pytest.fixture
def testcase_3():
    return {"input": [[2, 8, 7], [7, 1, 3], [1, 9, 5]], "output": 17}
