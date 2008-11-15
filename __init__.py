import logging


DEF_COLOR="[0m"
BLUE="[34;01m"
CYAN="[36;01m"
GREEN="[32;01m"
RED="[31;01m"
GRAY="[37;01m"
YELLOW="[33;01m"

logging.addLevelName(logging.DEBUG,    CYAN   + '>> DEBUG')
logging.addLevelName(logging.INFO,     GREEN  + '>> INFO')
logging.addLevelName(logging.WARNING,  YELLOW + '>> WARNING')
logging.addLevelName(logging.ERROR,    RED    + '>> ERROR')
logging.addLevelName(logging.CRITICAL, RED    + '>> CRITICAL')
logging.basicConfig(level=logging.DEBUG, format=' %(levelname)-19s' + DEF_COLOR + ' %(message)s')
