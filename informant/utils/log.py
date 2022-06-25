from datetime import datetime
from enum import Enum

from classes.bcolors import bcolors


class LogType:
    ERROR = "ERROR"
    INFO = "INFO"
    WARNING = "WARNING"

def log(log_type: LogType, text: str, use_timer: bool = True):
    color = get_log_color(log_type)
    print(f"{color}[{log_type}]{get_spaces_amount(log_type)}", end=f"{bcolors.ENDC}")
    
    if use_timer:
        print(f"[{get_current_time()}] ", end='')
    
    print(text)
    
def get_log_color(log_type: LogType):
    if log_type == LogType.ERROR:
        return bcolors.FAIL

    if log_type == LogType.INFO:
        return bcolors.OKCYAN

    if log_type == LogType.WARNING:
        return bcolors.WARNING

def get_spaces_amount(log_type: LogType):
    if log_type == LogType.ERROR:
        return "   " #3

    if log_type == LogType.INFO:
        return "    " #4

    if log_type == LogType.WARNING:
        return ' '# 1
   
def get_current_time():
    dt_string = datetime.now().strftime("%H:%M:%S")
    return dt_string
        
