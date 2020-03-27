import re

def stripper (string, rem=' '):
    matches = None

    wordRegex = re.compile(r'(\S+)')

    if rem == ' ':
        matches = wordRegex.findall(string)
        newstring = ' '.join(matches)
    else:
        #if rem == '\n':
            #otherRegex = re.compile(r'[^\n')
        #elif rem in ('.', '*', '?', '+', '^', '|' ):
            #otherRegex = re.compile('\' + rem)
        otherRegex = re.compile(r'[^'+ rem + ']')

        matches = otherRegex.findall(string)
        newstring = ''.join(matches)
    
    print(newstring)
    return newstring

stripper('heyyy adsdas99', '99')