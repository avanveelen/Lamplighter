import json
import datetime
from datetime import datetime, timedelta
import requests

class Sunset:
    '''Checks if the sun is set'''

    def is_the_sun_set(self):
        '''Returns true when the sun is set'''
        url = 'https://api.sunrise-sunset.org/json?lat=51.9244201&lng=4.4777325&date=today'
        result = requests.get(url)
        data = json.loads(result.content.decode('utf-8'))
        return self.__is_it_dark(data['results']['sunset'], data['results']['sunrise'])

    def __is_it_dark(self, sunset, sunrise):
        now_time = datetime.utcnow().time()
        sunset_time = (datetime.strptime(sunset, '%I:%M:%S %p') + timedelta(hours=-1)).time()
        sunrise_time = datetime.strptime(sunrise, '%I:%M:%S %p').time()
        return now_time >= sunset_time or now_time <= sunrise_time
