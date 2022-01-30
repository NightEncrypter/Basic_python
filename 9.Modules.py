# A basically a file containing a set of functions to include in your application, There are core python modules,modules you can install using pip package manager (including Django) as well as custom modules


# import datetime
# import time
import cmodule

# Specific import
from datetime import date
from time import time
from cmodule import checklen


# Pip modules
from camelcase import CamelCase

# Custom modules
# print(cmodule.checklen("hello"))
print(checklen("hello"))


# Modules
camel = CamelCase()
text = "hello there world"
print(camel.hump(text))
# today = date.today()
# print(today)

# timestamp=time.time()
timestamp = time()

print(timestamp)
