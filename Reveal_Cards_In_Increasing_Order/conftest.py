import pytest


@pytest.fixture
def testcase_1():
    return {"input": [17, 13, 11, 2, 3, 5, 7], "output": [2, 13, 3, 11, 5, 17, 7]}


@pytest.fixture
def testcase_2():
    return {"input": [1, 1000], "output": [1, 1000]}
