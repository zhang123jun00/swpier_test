import random
def get_code(num):
    code = random.randrange(10**(num-1),10**num - 1)
    return  code