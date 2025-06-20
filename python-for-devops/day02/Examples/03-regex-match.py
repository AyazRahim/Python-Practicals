import re

text = "one minute down second minute up"
pattern = r"one"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("match not found")

    #-----

import re
text = "not a man you won't to drop"
pattern = r"drop"

match = re.match(pattern, text)
if match:
     print("match found:", match.group())
else:
     print("match not found")
