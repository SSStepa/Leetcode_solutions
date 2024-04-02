from .Fizz_Buzz import fizzBuzz


def test(testcase_1, testcase_2, testcase_3):
    assert fizzBuzz(testcase_1["input"]) == testcase_1["output"]
    assert fizzBuzz(testcase_2["input"]) == testcase_2["output"]
    assert fizzBuzz(testcase_3["input"]) == testcase_3["output"]
