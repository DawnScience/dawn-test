from pprint import pprint
import sys

pprint(sys.path)

# We have this sleep in here so that it is visually easy to see that
# all the actors are running in parallel
import time
time.sleep(3)

import mymodule as lib_module
def run(**kwargs):
    if lib_module.modfunc() != 3:
        raise Exception("Wrong lib_module imported")
    # Return c = 3 so that we can check that in the output
    return {'c': 3}
