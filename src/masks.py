import logging

logger = logging.getLogger("masks")
file_handler = logging.FileHandler("../logs/masks.log", "a", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    logger.info("Создаём маскировку карты")
    if len(card_number) == 16 and card_number.isdigit():
        logger.info("Маскировка создана")

        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    logger.error("Ошибка, некорректный ввод")
    raise ValueError("Номер карты введён не корректно")


def get_mask_account(mask_account: str) -> str:
    """Функция маскировки номера банковского счета"""
    logger.info("Создаём маскировку счёта")
    if len(mask_account) == 20 and mask_account.isdigit():
        logger.info("Маскировка создана")
        return f"**{mask_account[16:]}"
    logger.error("Ошибка,номер счёта введён не корректно")
    raise ValueError("Номер счёта введён не корректно")


print(get_mask_card_number("1203142289606361"))
print(get_mask_account("73654108430135874305"))
