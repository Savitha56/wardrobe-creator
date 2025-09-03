import json
import os

# Check if file exists
if os.path.exists("users_data.json"):
    with open("users_data.json", "r") as file:
        all_users = json.load(file)
else:
    print("No data file found.")
    all_users = {}

# Ask which user to delete
name_to_delete = input("Enter the name of the user to clear data: ")

if name_to_delete in all_users:
    confirm = input(f"Are you sure you want to delete data for {name_to_delete}? (yes/no): ")
    if confirm.lower() == "yes":
        del all_users[name_to_delete]  # remove user data
        with open("users_data.json", "w") as file:
            json.dump(all_users, file, indent=4)
        print(f"Data for {name_to_delete} has been cleared.")
    else:
        print("Deletion cancelled.")
else:
    print(f"No data found for user: {name_to_delete}")
