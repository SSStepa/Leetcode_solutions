import pytest


@pytest.fixture
def testcase_1():
    return {"input": 121, "output": True}


@pytest.fixture
def testcase_2():
    return {"input": -121, "output": False}


@pytest.fixture
def testcase_3():
    return {"input": 10, "output": False}


@pytest.fixture
def testcase_4():
    return {"input": -2 ** 31, "output": False}


@pytest.fixture
def testcase_5():
    return {"input": (2 ** 31 - 1), "output": False}

