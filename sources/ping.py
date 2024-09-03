__author__ = "eolus87"

# Standard libraries

# Third party libraries
from ping3 import ping

# Custom libraries

def ping_function(target: str) -> float:
    response = ping(target, unit='ms', timeout=2)
    if response is None or response is False:
        return 2000.0  # Return 2000ms for unreachable targets
    return response