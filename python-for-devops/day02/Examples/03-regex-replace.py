import re

text = "The quick brown fox jumps over the lazy brown dog"
pattern = r"brown"

replacement = "red"

new_text = re.sub(pattern, replacement, text)

print("The Modified Text:", new_text)


#--------------

import re

text = " i am Ayaz Rahim, from lower kurram agency bilyamin"
pattern = r" lower kurram agency"

replacement = "Islamic Republic of pakistan"

new_address = re.sub(pattern, replacement, text)

print("The Current address is:", new_address)

