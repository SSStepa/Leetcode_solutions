import pytest


@pytest.fixture
def testcase_1():
    return {"input": ([2, 3, 2], 2), "output": 6}


@pytest.fixture
def testcase_2():
    return {"input": ([5, 1, 1, 1], 0), "output": 8}
