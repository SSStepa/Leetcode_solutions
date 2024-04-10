from .Reveal_Cards_In_Increasing_Order import deckRevealedIncreasing


def test(testcase_1, testcase_2):
    assert deckRevealedIncreasing(testcase_1["input"]) == testcase_1["output"]
    assert deckRevealedIncreasing(testcase_2["input"]) == testcase_2["output"]
