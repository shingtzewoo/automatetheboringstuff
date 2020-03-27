import re

#regular expression to detect days, months, years
#month, day, year
#regex to detect or if statements to detect if code is correct

dateRegex = re.compile(r'([0-3][0-9])[/]([0-1][1-9])[/]([1-2][0-9][0-9][0-9])')

date = '11/12/999'

try:

    days, month, year = dateRegex.search(date).groups()

    if int(month) in [4, 6, 8, 11]:
        if int(days) > 30:
            print('Invalid date. For April, June, September, and November there are only 30 days.')
        else:
            print('Your date: %s/%s/%s is valid' % (days, month, year))
    elif int(month) in [1, 3, 5, 7, 9, 10, 12]:
        if int(days) > 31:
            print('Invalid date. For January, March, May, July, August, October, and December there are only 31 days.')
        else:
            print('Your date: %s/%s/%s is valid' % (days, month, year))
    elif int(month) == 2:
        if (int(year) % 4 == 0 and (int(year) % 100 != 0 or (int(year) % 100 == 0 and int(year) % 400 == 0))):
            if int(days) >  29:
                print('Invalid date. For leap years, February has 29 days.')
            else:
                print('Your date: %s/%s/%s is valid' % (days, month, year))
        else:
            if int(days) > 28:
                print('Invalid date. February has 28 days.')
            else:
                print('Your date: %s/%s/%s is valid' % (days, month, year))

except AttributeError:
    print('Please put a valid date.')

#checking if dates are valid
#checking if month and days are valid
#leap year check
    


