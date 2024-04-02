import pytest


@pytest.fixture
def testcase_1():
    return {"input": [1, 2, 3], "output": 6}


@pytest.fixture
def testcase_2():
    return {"input": [1, 2, 3, 4], "output": 24}


@pytest.fixture
def testcase_3():
    return {"input": [-1, -2, -3], "output": -6}

