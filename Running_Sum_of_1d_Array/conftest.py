import pytest


@pytest.fixture
def testcase_1():
    return {"input": [1, 2, 3, 4], "output": [1, 3, 6, 10]}


@pytest.fixture
def testcase_2():
    return {"input": [1, 1, 1, 1, 1], "output": [1, 2, 3, 4, 5]}


@pytest.fixture
def testcase_3():
    return {"input": [3, 1, 2, 10, 1], "output": [3, 4, 6, 16, 17]}
