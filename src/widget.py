from typing import Any
from .masks import get_mask_account
from .masks import get_mask_card_number

card_number = str(input())


def mask_account_card(arg: Any) -> str:
    """Функция обработки информации о картах и счетах"""

    cn = card_number.split(" ")
    if "счет" in cn[0].lower():
        b_number = get_mask_account(cn[-1])
        new_card = cn[0] + " " + b_number
    else:
        b_number = get_mask_card_number(cn[-1])
        cn = " ".join(cn[:-1])
        new_card = cn + " " + b_number
    return new_card


def get_date(d: str) -> str:
    """Функция сортировки по дате"""
    date_time = d.split("T")[0]
    d_time = f"{date_time[-2:]}.{date_time[5:7]}.{date_time[:4]}"
    return d_time
