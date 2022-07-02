import time
import sys

from utils.log import log

class Globals():
    request_amount = 0

def await_after_multiple_calls(call_amount: int):
    if Globals.request_amount >= call_amount:
        log.warning("Request amound passed")
        time.sleep(5)
        Globals.request_amount = 0
    Globals.request_amount += 1
    
    log.warning(f"Counting request amound: {Globals.request_amount}")
        
        