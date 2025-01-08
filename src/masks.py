def get_mask_card_number(card_number: str) -> str:
    """Функцию маскировки номера банковской карты"""
    new_card_number = ""
    number_part1 = ""
    number_part2 = ""
    number_part3 = ""

    for el in card_number[:4]:
        number_part1 += el
    new_card_number += number_part1 + " "
    for el in card_number[4:6]:
        number_part2 += el
    new_card_number += number_part2 + "**" + " " + "****" + " "
    for el in card_number[12:]:
        number_part3 += el
    new_card_number += number_part3
    return new_card_number


def get_mask_account(card_number: str) -> str:
    """Функцию маскировки номера банковского счета"""
    new_card_number = ""
    number_part = ""

    for el in card_number[12:]:
        number_part += el
    new_card_number = "**" + number_part
    return new_card_number
