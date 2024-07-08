import random
import time
from worker import call_by_worker
def get_code(num):
    code = random.randrange(10**(num-1),10**num - 1)
    return  code

@call_by_worker
def send_verify_code():
    time.sleep(5)
    return get_code(4)

