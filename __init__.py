# coding: utf-8
import logging


DEF_COLOR="\x1b[0m"
BLUE="\x1b[34;01m"
CYAN="\x1b[36;01m"
GREEN="\x1b[32;01m"
RED="\x1b[31;01m"
GRAY="\x1b[37;01m"
YELLOW="\x1b[33;01m"

logging.addLevelName(logging.DEBUG,    CYAN   + '>> DEBUG')
logging.addLevelName(logging.INFO,     GREEN  + '>> INFO')
logging.addLevelName(logging.WARNING,  YELLOW + '>> WARNING')
logging.addLevelName(logging.ERROR,    RED    + '>> ERROR')
logging.addLevelName(logging.CRITICAL, RED    + '>> CRITICAL')
logging.basicConfig(level=logging.DEBUG, format=' %(levelname)-19s' + DEF_COLOR + ' %(message)s')
