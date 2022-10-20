import string




def check_password(password):
    #fool-proof
    if not isinstance(password, str) or len(password.strip()) == 0:
        return -1

    password = password.strip()
    digit = string.digits
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    #logic
    if len(password) < 8:
        return "too weak"

    #weak
    is_digit = True
    if (all([ch in digit for ch in password])
            or all([ch in lower for ch in password])
            or all([ch in upper for ch in password])):
        return "weak"


    #VERY STRONG
    if (any([ch in digit for ch in password])
                and any([ch in lower for ch in password])
               and any([ch in upper for ch in password])):
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










