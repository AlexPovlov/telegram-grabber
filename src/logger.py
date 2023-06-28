import logging

from .conf import path_errors

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

# Создание обработчика для записи в файл
file_handler = logging.FileHandler(path_errors)
file_handler.setLevel(logging.ERROR)

# Создание форматтера
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

# Добавление обработчика в логгер
logger.addHandler(file_handler)
