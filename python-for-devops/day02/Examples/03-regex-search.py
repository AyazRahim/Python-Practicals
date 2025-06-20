
import re
text = "The quick brown fox"
pattern = r"fox"

search = re.search(pattern , text)
if search:
    print("Pattern Found:", search.group())
else:
    print("Pattern Not Found")

    #------------------------

import re
text = " i am me and that my power"
pattern = r"power"

search = re.search(pattern, text)
if search:
    print("Pattern1 Found:", search.group())
else:
        print("Pattern1 Not Found")


import re
numbs = (1 , 2 ,3)
pattern = r'3'

search = re.search(pattern, ' '.join(map(str, numbs)))
if search:
    print("pattern2 found:", search.group())

else:
    print("patternt2 not found")

