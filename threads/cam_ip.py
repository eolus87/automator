__author__ = "Eolus87"

# Standard libraries
import time

# Third party libraries

# Custom libraries


class plug_ip:
    def __init__(self, config: dict):
        self.plug_ip = config["cam_ip"]
        self.plug_type = config["cam_type"]
        self.target_ip = config["target_ip"]
        self.polling_rate = config["polling_rate"]

        self.keep_running = True

    def run(self):
        while self.keep_running:


            time.sleep(1/self.polling_rate)
