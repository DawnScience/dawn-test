from pprint import pprint
import sys

pprint(sys.path)

# We have this sleep in here so that it is visually easy to see that
# all the actors are running in parallel
import time
time.sleep(3)

import mymodule as src2_module
import src1.mymodule as src1_module
def run(**kwargs):
    if src2_module.modfunc() != 2:
        raise Exception("Wrong src2_module imported")
    if src1_module.modfunc() != 1:
        raise Exception("Wrong src1_module imported")
    # Return b = 2 so that we can check that in the output
    return {'b': 2}
