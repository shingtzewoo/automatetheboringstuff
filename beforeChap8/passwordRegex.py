import re

def passwordChecker (password):

    capitalRegex = re.compile(r'[A-Z]+')
    lowerRegex = re.compile(r'[a-z]+')
    digitRegex = re.compile(r'[0-9]+')

    #checking against regex

    if capitalRegex.search(password) != None:
        capitalCheck = 'Pass'
    else:
        capitalCheck = 'Fail'
        print('Your password does not contain any capital letters')
    
    if lowerRegex.search(password) != None:
        lowerCheck = 'Pass'
    else:
        lowerCheck = 'Fail'
        print('Your password does not contain any lowercase letters')

    if digitRegex.search(password) != None:
        digitCheck = 'Pass'
    else:
        digitCheck = 'Fail'
        print('Your password does not contain any digits')

    for check in (capitalCheck, lowerCheck, digitCheck):
        if check == 'Fail':
            print("Your password sucks!")
            return False
    
    print("Your password is good")
    return True
    

passwordChecker('123aA')