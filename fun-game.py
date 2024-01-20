import webbrowser
import time

# Number of times to open the browser
num_openings = 100

# Delay between openings (in seconds)
delay = 0.5

# URL to open
url = "https://example.com"
url2 = "https://g.co/kgs/uTTZvBg"
url3 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS0_SApr5DBJWlm0I90kDye5Sr-0cPp_sM0Rg&usqp=CAU"
url4 = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTpByXQhWAEaWCHuy_RZuf-gBdTuZPYjBmxzA&usqp=CAU"

# Open the browser multiple times
for _ in range(num_openings):
    webbrowser.open(url)
    webbrowser.open(url2)
    webbrowser.open(url3)
    webbrowser.open(url4)
    time.sleep(delay)