from config import config
import logging
import logging.config

logging.config.dictConfig(config['log'])
