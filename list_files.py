import os

# Take input and split it into a list of folder names
folders = input("Please enter folder names with spaces between them: ").split()

print("You entered:", folders)

for folder in folders:
    try:
        files = os.listdir(folder)  # list the contents of the folder
        print(f"Files in '{folder}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"No such folder: '{folder}'")
    except PermissionError:
        print(f"Permission denied: '{folder}'")
