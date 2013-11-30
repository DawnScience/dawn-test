from pprint import pprint
import sys

pprint(sys.path)

# We have this sleep in here so that it is visually easy to see that
# all the actors are running in parallel
import time
time.sleep(3)

import myothermodule as local_module
def run(**kwargs):
    if local_module.modfunc() != 5:
        raise Exception("Wrong local_module imported")
    # Return e = 5 so that we can check that in the output
    return {'e': 5}
