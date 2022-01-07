# Webscraping
#! python3
# weatherToday.py - Launches a weather report in the browser using a city from the
# command line or clipboard.

import webbrowser, sys, pyperclip
pyperclip.copy('https://weather.com/weather/today/l/13c98a0c1ca5b22d2918f6c90648c70fd6f903f7694699d20bc46ea6b575711a')

if len(sys.argv) > 1:
    # Get city from command line.
    city = ' '.join(sys.argv[1:])
    webbrowser.open('https://weather.com/weather/today/' + city)
else:
    # Get city from clipboard
    city = pyperclip.paste()
    webbrowser.open(city)

