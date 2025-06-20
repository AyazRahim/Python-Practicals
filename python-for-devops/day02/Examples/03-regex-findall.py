import re

text = "one minute down second minute up"
pattern = r"minute"

finds = re.findall(pattern, text)

if finds:
    print("All found:", finds)
    print("Total matches:", len(finds))
else:
    print("No matches found")
