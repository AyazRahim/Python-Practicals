import re

text = "apple,orange,banana,mango"
pattern = r","

split_result = re.split(pattern, text)
print("The splitted Result is:", split_result)


