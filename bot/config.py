from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", "28614709"))
    API_HASH = env.get("TELEGRAM_API_HASH", "f36fd2ee6e3d3a17c4d244ff6dc1bac8")
    OWNER_ID = int(env.get("OWNER_ID", "7970350353"))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "Mikotsbot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "7540338860:AAF7xysL_W9Mn27sQwsXyIUV8q0RwTfu_Qs")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", "-1002669902570"))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 24))

class Server:
    BASE_URL = env.get("BASE_URL", "http://139.59.248.28:8220")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", "8220"))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'hydrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
