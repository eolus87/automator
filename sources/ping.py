__author__ = "Eolus87"

# Standard libraries
from typing import List, Union

# Third party libraries
from pythonping import ping

# Custom libraries


def ping_function(target: str) -> float:
    response = ping(target, count=1, verbose=False)
    return response.rtt_avg_ms