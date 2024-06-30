import json

# Define JSON file path
file_path = "tasks.json"

# Read JSON file and load it into a variable
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    print("File path not found or file is empty/invalid, initializing with an empty tasks list.")
    data = {"tasks": []}

