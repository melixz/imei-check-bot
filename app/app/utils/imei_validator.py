def is_valid_imei(imei: str) -> bool:
    if len(imei) != 15 or not imei.isdigit():
        return False

    total = 0
    for i, ch in enumerate(imei[:-1]):
        digit = int(ch)
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    check_digit = (10 - (total % 10)) % 10
    return check_digit == int(imei[-1])
