# Default log level
LOG_LEVEL = "INFO"

# URL containing menu pics
COLLEGE_HOST = "https://collegetsaritsyno.mskobr.ru"
MENU_PATH = "/roditelyam/vse-voprosi-o-pitanii"

# Bot class
# - menubot.bots.TelegramBot - Telegram
# - menubot.bots.VkBot - VK
BOT_CLASS = "menubot.bots.TelegramBot"

# Bot token
BOT_API_KEY = "secret"

# Database URI for sqlalchemy
DATABASE_URI = "sqlite+aiosqlite:///menubot.sqlite"

try:
    from .local_config import *  # noqa
except ImportError:
    pass
