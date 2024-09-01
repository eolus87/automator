__author__ = "Eolus87"

# Standard libraries
import time
import json

# Third party libraries
import requests

# Custom libraries

MIN_REQUEST_INTERVAL = 10800
DAYTIME_START_DELAY = 0
DAYTIME_END_DELAY = 0


class DawnDask:
    """Class to get sunrise and sunset times from the internet. 
    The class uses the API provided by https://sunrise-sunset.org/
    to get the sunrise and sunset times for a given location and date.
    
    The class has a protection mechanism to avoid making too many requests.
    
    The API is free, but requires attribution and citing them as the source.
    """
    
    def __init__(self, latitude: float, longitude: float, tzid: str):
        # REST API location and timezone
        self.__latitude = latitude
        self.__longitude = longitude
        self.__tzid = tzid
        # Protection mechanism
        self.__api_latest_request = 0
        self.__dawn_time = ""
        self.__dusk_time = ""
        # state_variable
        self.__is_daytime = False
    
    def __is_update_required(self) -> bool:
        update_required = False
        
        tic = time.time()
        if tic - self.__api_latest_request > MIN_REQUEST_INTERVAL:
            update_required = True
        
        return update_required

    def __update_state(self):
        if self.__is_update_required():
            self.__api_latest_request = tic
            response = requests.get(request_string)
            response_dict = json.loads(response.text)
            # TODO: change the strings of reponsde by time.time comparable
            self.__dawn_time = response_dict['results']['sunrise']
            self.__dusk_time = response_dict['results']['sunset']
    
    def has_daytime_started(self) -> bool:
        is_daytime = copy.copy(self.__is_daytime)
        
        self.__update_state()
        daytime_start = self.__dawn_time + DAYTIME_START_DELAY
        daytime_end = self.__dusk_time + DAYTIME_END_DELAY
        tic = time.time()
        if daytime_start < tic < daytime_end:
            self.__is_daytime = True
        else:
            self.__is_daytime = False
        
        return self.__is_daytime and not self.__is_daytime

    def get_dawn_dusk(self) -> dict:
        request_string = \
            f"https://api.sunrise-sunset.org/json?" \
            f"lat={self.__latitude}" \
            f"&lng={self.__longitude}" \
            f"&date=today" \
            f"&tzid={self.__tzid}"
        
        tic = time.time()
        if tic - self.__api_latest_request > MIN_REQUEST_INTERVAL:
            
        
        return {"dawn": self.dawn, "dusk": self.dusk}

        
