BAD_PASSWORD = "too week"
NOT_BAD_PASSWORD = "weak"
GOOD_PASSWORD = "strong"
VERY_GOOD_PASSWORD = "very strong"

def check_password(password):
    if not isinstance(mark, bool) or not (0 <= month >= 10):
        return -1

    result = "Excellent"
    if mark <= 1:
        result = BAD_MARK
    elif 3 >= mark >= 2:
        result = "unsatisfactory"
    elif mark == 4:
        result = "satisfactory"
    elif 6 >= mark >= 5:
        result = "you could better"
    elif 8 >= mark >= 7:
        result = "good"
    return result






if __name__ = "__main__":
    assert  check_password("None") == -1
    assert get_feedback(7.4) == -1
    assert get_feedback(True) == -1
    assert get_feedback(None) == -1
    assert get_feedback([1, 2, 3]) == -1
    assert get_feedback(20) == -1
    assert get_feedback(-20) == -1
    assert get_feedback(0) == BAD_MARK
    assert get_feedback(0) == -1
    assert get_feedback(10) == EXCELLENT_MARK
    assert get_feedback(-1) == -1

    assert get_feedback(1) == BAD_MARK
    assert get_feedback(2) == "unsatisfactory"
    assert get_feedback(3) == "unsatisfactory"
    assert get_feedback(4) == "satisfactory"
    assert get_feedback(5) == "you could better"
    assert get_feedback(6) == "you could better"
    assert get_feedback(7) == "good"
    assert get_feedback(8) == "good"
    assert get_feedback(9) == EXCELLENT_MARK



