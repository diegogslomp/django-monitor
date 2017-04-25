# Days to change the status from red (danger) to yellow (warning)
DAYS_FROM_DANGER_TO_WARNING = 5
# Time to wait after each host check in seconds (0..)
WAIT_FOR_NEXT = 0.5
# Max log lines for each host
MAX_LOG_LINES = 20
# User for telnet login
USER = 'admin'
# Password for telnet login
PASSWORD = 'secret'

try:
    from .local import *
except ImportError:
    pass
