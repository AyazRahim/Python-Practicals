import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_details = response.json()

for elements in range(len(complete_details)):

    print(complete_details[elements]["user"]["login"])