# URL с разделом меню
MENU_URL = "https://collegetsaritsyno.mskobr.ru/roditelyam/vse-voprosi-o-pitanii"

# Текущий учебный год (2022 - 2022/2023). Для определения года, если его нет
CURRENT_YEAR = 2022

# Таймаут запросов в секундах
TIMEOUT = 5

# Ключ для Telegram-бота
BOT_API_KEY = "secret"

# Прокси
PROXY_TYPE = "socks5"
PROXY_IP = "localhost"
PROXY_PORT = "8080"

# sqlite
DATABASE_URI = "sqlite:///menubot.sqlite"

try:
    from .local_config import *  # noqa
except ImportError:
    pass
