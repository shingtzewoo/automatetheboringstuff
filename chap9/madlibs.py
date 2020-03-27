import sys, os

import pyinputplus as pyip

from pathlib import Path

# This program reads files and lets users replace words ADJECTIVE, NOUN, ADVERB, or VERB with any text they want
# Usage: python madlibs.py textfile.txt

# example:
# The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was unaffected by these events. 
# AFTER
# The silly panda walked to the chandelier and then screamed. A nearby pickup truck was unaffected by these events.

if len(sys.argv) < 2 or len(sys.argv) >= 3:

    print('Usage: python madlibs.py textfile.txt')

else:
    
    my_file = Path(Path.cwd() / sys.argv[1])

    # checking if the file exists
    if my_file.is_file():

        #getting the words from the text file
        my_file = open(my_file, 'r')

        words = my_file.read().split()

        my_file.close()

        # getting the non-letters such as punctuations, exclamation marks, etc.
        suffixNonLetters = {}

        for index, value in enumerate(words):
            if not value[-1].isalpha():
                suffixNonLetters.setdefault(index, value[-1])
                words[index] = value[:-1]
        
        print(suffixNonLetters)
        print(words)

        
        if any(word in ['adjective', 'noun', 'verb', 'adverb'] for word in words):

            for index, value in enumerate(words):
                if value.lower() in ['adjective', 'noun', 'verb', 'adverb']:
                    if value.lower() == 'adjective':
                        adjective = pyip.inputStr('Enter an adjective: ', allowRegexes=[r'[A-Za-z]'])
                        words[index] = adjective
                    elif value.lower() == 'noun':
                        noun = pyip.inputStr('Enter a noun: ', allowRegexes=[r'[A-Za-z]'])
                        words[index] = noun
                    elif value.lower() == 'verb':
                        verb = pyip.inputStr('Enter a verb: ', allowRegexes=[r'[A-Za-z]'])
                        words[index] = verb
                    elif value.lower() == 'adverb':
                        adverb = pyip.inputStr('Enter an adverb: ', allowRegexes=[r'[A-Za-z]'])
                        words[index] = adverb
                else:
                    continue
            
            # adding non-letters back to the words
            for key, value in suffixNonLetters.items():
                words[key] = words[key] + value

            words = " ".join(words)

            # writing to the file
            my_file = Path(Path.cwd() / sys.argv[1])
            my_file = open(my_file, 'w')
            my_file.write(words)
            my_file.close()
                
        else:
            print("None of the replacement words are in the textfile")
    else:
        print("Your file does not exist! Please use on an existing file.")