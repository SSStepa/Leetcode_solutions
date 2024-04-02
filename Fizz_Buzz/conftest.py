import pytest


@pytest.fixture
def testcase_1():
    return {"input": 3, "output": ["1", "2", "Fizz"]}


@pytest.fixture
def testcase_2():
    return {"input": 5, "output": ["1", "2", "Fizz", "4", "Buzz"]}


@pytest.fixture
def testcase_3():
    return {
        "input": 15,
        "output": ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
    }
