from .Time_Needed_to_Buy_Tickets import timeRequiredToBuy


def test(testcase_1, testcase_2):
    assert timeRequiredToBuy(testcase_1["input"][0], testcase_1["input"][1]) == testcase_1["output"]
    assert timeRequiredToBuy(testcase_2["input"][0], testcase_2["input"][1]) == testcase_2["output"]
