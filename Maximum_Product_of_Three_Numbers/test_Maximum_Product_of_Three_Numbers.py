from .Maximum_Product_of_Three_Numbers import maximumProduct


def test(testcase_1, testcase_2, testcase_3):
    assert maximumProduct(testcase_1["input"]) == testcase_1["output"]
    assert maximumProduct(testcase_2["input"]) == testcase_2["output"]
    assert maximumProduct(testcase_3["input"]) == testcase_3["output"]
