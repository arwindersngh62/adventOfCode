from sol2 import get_score,get_common
import pytest


@pytest.mark.parametrize("input, score", [("p", 16), ("L", 38), ("P", 42)])
def test_get_score(input, score):
    assert get_score(input) == score


@pytest.mark.parametrize("str1,str2,str3, common", [("vJrwpWtwJgWrhcsFMMfFFhFp","jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL", "PmmdzqPrVvPwwTWBwg", "r")])    
def test_get_commons(str1, str2, str3, common):
    assert get_common(str1, str2, str3) == common
    