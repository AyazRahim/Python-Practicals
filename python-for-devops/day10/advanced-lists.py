import os


folders = input("Enter a list of folders separatd by spaces: ").split()

for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please Provide a valid directory name")
        continue
    except PermissionError:
        print("You do not have the required permission:"  + folder)
        continue
    print(" ===>>> Listing file for the directory _ " + folder)


    for file in files:
        print(file)

