#! python
# vanweather.py opens up Vancouver Accuweather site for the hourly weather forecast depending on the chosen day of the week 
# works for this week up until the day before the next week's chosen day

import sys, webbrowser, datetime

chrome_path = 'open -a /Applications/Google\ Chrome.app %s' # taken from https://stackoverflow.com/questions/22445217/python-webbrowser-open-to-open-chrome-browser

today = datetime.date.today().weekday()
weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

if len(sys.argv) > 1:
    
    day_wanted = sys.argv[1].lower()

    if day_wanted not in weekdays:
        print("valid day has to be chosen")
        sys.exit()

else:
    print("Usage: python3 vanweather.py chosen_day")
    sys.exit()

today = weekdays[today]

if day_wanted == today:
    webbrowser.get(chrome_path).open('https://www.accuweather.com/en/ca/vancouver/v6c/hourly-weather-forecast/53286?day=1')
else:
    day = weekdays.index(day_wanted)
    today = weekdays.index(today)

    if int(day) > int(today):
        diff = int(day) - int(today) + 1 # adding 1 because accuweather uses 0 and 1 as the argument for today in their address
        webbrowser.get(chrome_path).open(f'https://www.accuweather.com/en/ca/vancouver/v6c/hourly-weather-forecast/53286?day={diff}')
    elif int(day) < int(today):
        
        front_diff = len(weekdays) - 1 - int(today)
        back_diff = int(day) + 2

        # AccuWeather only shows hourly weather forecasts for up to two days in advance, so if the chosen day is further away, it directs users to the daily weather forecast
        if front_diff + back_diff > 3:
            webbrowser.get(chrome_path).open(f'https://www.accuweather.com/en/ca/vancouver/v6c/daily-weather-forecast/53286?day={front_diff + back_diff}')
        else:
            webbrowser.get(chrome_path).open(f'https://www.accuweather.com/en/ca/vancouver/v6c/hourly-weather-forecast/53286?day={front_diff + back_diff}')






