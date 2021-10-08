import random

def problem2_4():
    """ Make a list of 10 random reals between 30 and 35 """
    random.seed(70)
    lis=[0] * 10
    for i in range(10):
        numone = random.random()
        numone = numone*5
        numone = numone+30
        lis[i] = numone
    print(lis)