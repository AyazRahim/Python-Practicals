import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

#print(response.status_code)

###-----   Also be possible to print in diff format   -----###
print(response.json())
#print(type(response))

