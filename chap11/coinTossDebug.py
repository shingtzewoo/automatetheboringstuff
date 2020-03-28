import logging
logging.basicConfig(level=logging.DEBUG, format='%(message)s')

import random
guess = ''
while guess not in ('heads', 'tails'): #guess can only be heads or tails, however, toss is a number
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    logging.debug(f"toss is {toss} and guess is {guess}")
    print('Nope! Guess again!')
    guesss = input() # guess has a typo, an extra s
    if toss == guess:
        logging.debug(f"toss is {toss} and guess is {guess}")
        print('You got it!')
    else:
        logging.debug(f"toss is {toss} and guess is {guess}")
        print('Nope. You are really bad at this game.')