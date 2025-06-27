import sys

type = sys.argv[1]

if type == "t2.micro":
    print("OKAY, but it will charge you $2 per day")
elif type == "t2.medium":
    print("This will charge you $4 per day")
elif type == "t2.large":
    print("This will charge you $8 per day")
else:
    print("Please Provide a valid instance type")