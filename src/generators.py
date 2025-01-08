def filter_by_currency(transactions, bill="RUB"):
    """Функция выдачи транзакции заданной валюты"""
    filter_bill = [el for el in transactions if el["operationAmount"]["currency"]["code"] == bill]
    yield filter_bill


def transaction_descriptions(transactions):
    """Функция выдачи описания каждой транзакции"""
    transaction = [el["description"] for el in transactions if el["description"] != "" or el["description"] != " "]
    yield transaction


def card_number_generator(el_start: int, el_stop: int):
    """Функция генератора номера баанковской карты"""
    nums = (
        x
        for x in range(el_start, (el_stop + 1))
        if el_start >= 0 and el_start <= el_stop and el_stop <= 9999999999999999
    )
    range_list = []
    for el in nums:
        str_el = str(el).zfill(16)
        result = str_el[:4] + " " + str_el[4:8] + " " + str_el[8:12] + " " + str_el[12:]
        range_list.append(result)
    yield "\n".join(range_list)
