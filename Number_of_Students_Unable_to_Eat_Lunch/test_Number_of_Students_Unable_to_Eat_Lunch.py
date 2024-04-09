from .Number_of_Students_Unable_to_Eat_Lunch import countStudents


def test(testcase_1, testcase_2):
    assert countStudents(testcase_1["input"][0], testcase_1["input"][1]) == testcase_1["output"]
    assert countStudents(testcase_2["input"][0], testcase_2["input"][1]) == testcase_2["output"]
