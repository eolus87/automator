__author__ = "eolus87"

# Standard libraries
import time
import json
import datetime
import zoneinfo

# Third party libraries
import requests

# Custom libraries

MIN_REQUEST_INTERVAL = 10800  # 3 hours


class SunriseSunset:
    """Class to get sunrise and sunset times from the internet. 
    The class uses the API provided by https://sunrise-sunset.org/
    to get the sunrise and sunset times for a given location and date.
    
    The class has a protection mechanism to avoid making too many requests.
    
    The API is free, but requires attribution and citing them as the source.
    """
    
    def __init__(self, latitude: float, longitude: float, tzid: str):
        # REST API location, timezone, date and request string
        self.__latitude = latitude
        self.__longitude = longitude
        self.__tzid = tzid
        self.__request_string = \
            f"https://api.sunrise-sunset.org/json?" \
            f"lat={self.__latitude}" \
            f"&lng={self.__longitude}" \
            f"&date=today" \
            f"&tzid={self.__tzid}" \
            f"&formatted=0"
        # Protection mechanism
        self.__api_latest_request = datetime.datetime.min
        self.sunrise_time = float('nan')
        self.sunset_time = float('nan')

    
    def __is_update_required(self) -> bool:
        toc = datetime.datetime.now()
        if toc - self.__api_latest_request > datetime.timedelta(seconds=MIN_REQUEST_INTERVAL):
            update_required = True
        else:
            update_required = False
        return update_required

    def __update_state(self):
        if self.__is_update_required():
            self.__api_latest_request = time.time()
            response = requests.get(self.__request_string)
            response_dict = json.loads(response.text)
            if response_dict['status'] == 'OK':
                self.sunrise_time = datetime.datetime.fromisoformat(response_dict['results']['sunrise'])
                self.sunset_time = datetime.datetime.fromisoformat(response_dict['results']['sunset'])
            else:
                raise Exception(f"Error getting sunrise and sunset times: {response_dict['status']}")
      
    def __get_current_time(self) -> datetime.datetime:
        # Get current time as seconds since midnight
        return datetime.datetime.now().replace(tzinfo=zoneinfo.ZoneInfo(self.__tzid))
    
    def is_daytime(self, time_shift_seconds: int = 0) -> bool:
        self.__update_state()
        current_time = self.__get_current_time()
        sunrise_shifted = self.sunrise_time + datetime.timedelta(seconds=time_shift_seconds)
        sunset_shifted = self.sunset_time + datetime.timedelta(seconds=time_shift_seconds)
        return sunrise_shifted <= current_time < sunset_shifted
    
    def is_nighttime(self, time_shift_seconds: int = 0) -> bool:
        self.__update_state()
        current_time = self.__get_current_time()
        sunset_shifted = self.sunset_time + datetime.timedelta(seconds=time_shift_seconds)
        sunrise_shifted = self.sunrise_time + datetime.timedelta(seconds=time_shift_seconds)
        return sunset_shifted <= current_time or current_time < sunrise_shifted
