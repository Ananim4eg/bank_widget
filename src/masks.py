import logging
import os


log_path = os.path.join(os.path.dirname(__file__), '..', 'logs', 'masks.log')

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(log_path, mode='w', encoding="UTF-8")
file_formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(number_card: int) -> str:
    """Маскирует номер карты"""
    if len(str(number_card)) == 16:
        logger.info("Маскировка номера кары")
        return f"{str(number_card)[:4]} {str(number_card)[4:6]}** **** {str(number_card)[-4:]}"
    else:
        logger.error("Неверный формат, введенных, данных")
        return "Неверный формат, введенных, данных"


def get_mask_account(number_account: int) -> str:
    """Маскирует номер счета"""
    if len(str(number_account)) == 20:
        logger.info("Маскировка номера счета")
        return f"**{str(number_account)[-4:]}"
    else:
        logger.error("Неверный формат, введенных, данных")
        return "Неверный формат, введенных, данных"
