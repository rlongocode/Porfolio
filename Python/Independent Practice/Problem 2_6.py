
import random

def problem2_6():
    """ Simulates rolling 2 dice 100 times """
    # Setting the seed makes the random numbers always the same
    # This is to make the auto-grader's job easier.
    random.seed(431)  # don't remove when you submit for grading
    pass # replace this pass (a do-nothing) statement with your code
    for i in range(100):
        firstdice = random.randint(1,6)
        seconddice = random.randint(1,6)
        total = firstdice + seconddice
        print(total)
   