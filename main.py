import requests
import json
from datetime import datetime

response = requests.get('https://api-web.nhle.com/v1/club-schedule/TOR/week/now') # Get schedule for the Toronto Maple Leafs

current_date = datetime.now().date() # get today's date

json_data = response.json() if response and response.status_code == 200 else None

def game_check():
    if json_data and 'games' in json_data:
        for game in json_data['games']:
            game_date = game['gameDate']
            if game_date == current_date:
                return True;
            else:
                return False;
            

