from .Palindrome_Number import isPalindrome


def test(testcase_1, testcase_2, testcase_3, testcase_4, testcase_5):
    assert isPalindrome(testcase_1["input"]) == testcase_1["output"]
    assert isPalindrome(testcase_2["input"]) == testcase_2["output"]
    assert isPalindrome(testcase_3["input"]) == testcase_3["output"]
    assert isPalindrome(testcase_4["input"]) == testcase_4["output"]
    assert isPalindrome(testcase_5["input"]) == testcase_5["output"]
