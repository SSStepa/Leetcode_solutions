from .Number_of_Steps_to_Reduce_a_Number_to_zero import numberOfSteps


def test(testcase_1, testcase_2, testcase_3, testcase_4, testcase_5):
    assert numberOfSteps(testcase_1["input"]) == testcase_1["output"]
    assert numberOfSteps(testcase_2["input"]) == testcase_2["output"]
    assert numberOfSteps(testcase_3["input"]) == testcase_3["output"]
    assert numberOfSteps(testcase_4["input"]) == testcase_4["output"]
    assert numberOfSteps(testcase_5["input"]) == testcase_5["output"]
