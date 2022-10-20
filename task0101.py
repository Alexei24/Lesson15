DIGITS = "0123456789"
LOWER_CASE = "qwertyuiopasdfghjklzxcvbnm"
UPPER_CASE = "QWERTYUIOPASDFGHJKLZXCVBNM"




def check_password(password):
    #fool-proof
    if not isinstance(password, str) or len(password.strip()) == 0:
        return -1

    password = password.strip()


    #logic
    if len(password) < 8:
        return "too weak"

    #weak
    is_digit = True
    for ch in password:
        if ch not in DIGITS:
            is_digit = False
            break

    is_lower = True
    for ch in password:
        if ch not in LOWER_CASE:
            is_lower = False
            break

    is_upper = True
    for ch in password:
        if ch not in UPPER_CASE:
            is_upper = False
            break

    if is_upper or is_digit or is_lower:
        return "weak"


    #VERY STRONG
    is_digit = False
    for ch in password:
        if ch in DIGITS:
            is_digit = True
            break

    is_lower = False
    for ch in password:
        if ch in LOWER_CASE:
            is_lower = True
            break

    is_upper = False
    for ch in password:
        if ch in UPPER_CASE:
            is_upper = True
            break

    if is_lower and is_upper and is_digit:
        return "very strong"

    return "strong"

if __name__ == "__main__":
    assert check_password("") == -1
    assert check_password(" ") == -1
    assert check_password(None) == -1
    #assert check_password("!$%^&") == -1
    assert check_password(10.5) == -1
    assert check_password(10) == -1
    assert check_password([1, 2, 3]) == -1

    assert check_password("qwerty") == "too weak"
    assert check_password("1234567") == "too weak"
    assert check_password("QWERTYU") == "too weak"
    assert check_password("21asa") == "too weak"
    assert check_password("g") == "too weak"

    assert check_password("12345678") == "weak"
    assert check_password("qwertyuip") == "weak"
    assert check_password("qwertyui") == "weak"
    assert check_password("QWERTYUI") == "weak"
    assert check_password("QWERTYUIP") == "weak"
    assert check_password("123456789") == "weak"

    assert check_password("1234asdY") == "very strong"
    assert check_password("1234asdYasd1234gfg") == "very strong"

    assert check_password("1234RTYU") == "strong"
    assert check_password("1234RTYUQWEQWEQWE") == "strong"
    assert check_password("1234asdf") == "strong"
    assert check_password("1234ASDASDFQFQW") == "strong"
    assert check_password("ASDDGFDSasdf") == "strong"
    assert check_password("asdfZXCV") == "strong"










