import requests
import json
from datetime import datetime
import schedule
import time
from win10toast import ToastNotifier


print('Running...')
toaster = ToastNotifier()

def job():
    response = requests.get('https://api-web.nhle.com/v1/club-schedule/TOR/week/now') # Get schedule for the Toronto Maple Leafs

    current_date = datetime.now().date() # get today's date

    json_data = response.json() if response and response.status_code == 200 else None # get the json data from the response

    def game_check():
        if json_data and 'games' in json_data:
            for game in json_data['games']:
                game_date = game['gameDate']
                if game_date == current_date:
                    return True
                else:
                    return False

    game_today = game_check()
    
    if game_today:
        toaster.show_toast('A&W Burger', 'There is a $2 Teen burger on the A&W App, go get it!', duration=10)
        print('There is a game today')
    else:
        toaster.show_toast('A&W Burger', 'There is no teen burger deal today! ', duration=10)
        print('There is no game today')
job() # run job once on startup

# Schedule the job every minute
# schedule.every(1).minutes.do(job)

# Schedule the job every 24 hours
schedule.every(24).hours.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)