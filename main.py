__author__ = "Eolus87"

# Standard libraries

# Third party libraries

# Custom libraries
from sinks.tapo_onoff import turn_on, turn_off

#%%
target_ip="192.168.0.49"
user_name="niguvaz@gmail.com"
password="pepegrillo8"
timezone="Europe/London"

turn_on(target_ip, user_name, password)