import pytest


@pytest.fixture
def testcase_1():
    return {"input": ([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]), "output": 3}


@pytest.fixture
def testcase_2():
    return {"input": ([1, 1, 0, 0], [0, 1, 0, 1]), "output": 0}
