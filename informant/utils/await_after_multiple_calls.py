import time
import sys

class Globals():
    request_amount = 0

def await_after_multiple_calls(call_amount: int):
    if Globals.request_amount >= call_amount:
        print("[AWAIT] " + str(Globals.request_amount), file=sys.stderr)
        time.sleep(5)
        Globals.request_amount = 0
    Globals.request_amount += 1
    
    print("[COUNT] " + str(Globals.request_amount), file=sys.stderr)
        
        