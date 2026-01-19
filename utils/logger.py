import logging
import sys
from colorama import Fore, Style, init

init(autoreset=True)

class AntigravityFormatter(logging.Formatter):
    """
    Custom logging formatter for that God-Tier terminal aesthetic.
    """
    
    FORMATS = {
        logging.DEBUG:    Fore.CYAN + "[DEBUG]   " + Style.RESET_ALL + " %(message)s",
        logging.INFO:     Fore.GREEN + "[INFO]    " + Style.RESET_ALL + " %(message)s",
        logging.WARNING:  Fore.YELLOW + "[WARNING] " + Style.RESET_ALL + " %(message)s",
        logging.ERROR:    Fore.RED + "[ERROR]   " + Style.RESET_ALL + " %(message)s",
        logging.CRITICAL: Fore.RED + Style.BRIGHT + "[CRITICAL]" + Style.RESET_ALL + " %(message)s"
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%Y-%m-%d %H:%M:%S')
        return formatter.format(record)

def setup_logger():
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(AntigravityFormatter())
    
    logger = logging.getLogger("BotTele")
    logger.setLevel(logging.INFO)
    logger.addHandler(handler)
    
    return logger

log = setup_logger()
