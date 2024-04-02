import pytest


@pytest.fixture
def testcase_1():
    return {"input": 1, "output": 1}


@pytest.fixture
def testcase_2():
    return {"input": 14, "output": 6}


@pytest.fixture
def testcase_3():
    return {"input": 8, "output": 4}


@pytest.fixture
def testcase_4():
    return {"input": 123, "output": 12}


@pytest.fixture
def testcase_5():
    return {"input": 10 ** 6, "output": 26}
