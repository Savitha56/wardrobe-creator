import json
import os

# Load existing users if file exists
if os.path.exists("users_data.json"):
    with open("users_data.json", "r") as file:
        all_users = json.load(file)
else:
    all_users = {}

# Ask user info
name = input("Enter your name: ")
print("Welcome", name)

# Check if user already exists
if name in all_users:
    print(f"Hello {name}, your previous data is:")
    print(json.dumps(all_users[name], indent=4))
    exit()  # Stop here if existing user
else:
    gender = int(input("Enter your gender \n1. Male \n2. Female\n"))
    age_group = int(input("Enter your age group \n1. 0-10 \n2. 10-25 \n3. 25 and above\n"))

# Store casual wear
print("First, store your casual wears:")
if gender==1:
    if age_group==1:
        shirts = {}
        num_shirts = int(input("How many T-Shirts do you have? "))
        for i in range(1, num_shirts + 1):
            color = input(f"Enter the colour of T-Shirt {i}: ")
            shirts[i] = color

        trousers = {}
        num_trousers = int(input("How many Trousers do you have? "))
        for i in range(1, num_trousers + 1):
            color = input(f"Enter the colour of Trousers {i}: ")
            trousers[i] = color

        # Store occasional/functional wear
        print("Second, store your occasional or functional wear dresses:")
        occasional_wear = {}
        num_occasional = int(input("How many occasional or functional wear dresses do you have? "))
        for i in range(1, num_occasional + 1):
            item = input(f"Enter the variety of dress {i}: ")
            occasional_wear[i] = item
    if age_group==2:
        tshirts = {}
        tnum_shirts = int(input("How many T-Shirts do you have? "))
        for i in range(1, tnum_shirts + 1):
            color = input(f"Enter the colour of T-Shirt {i}: ")
            tshirts[i] = color

        strousers = {}
        snum_trousers = int(input("How many Trousers do you have? "))
        for i in range(1, snum_trousers + 1):
            color = input(f"Enter the colour of Trousers {i}: ")
            strousers[i] = color

        # Store occasional/functional wear
        print("Second, store your occasional or functional wear dresses:")
        toccasional_wear = {}
        tnum_occasional = int(input("How many occasional or functional wear dresses do you have? "))
        for i in range(1, tnum_occasional + 1):
            item = input(f"Enter the variety of dress {i}: ")
            toccasional_wear[i] = item
        

# Combine all data for this user
user_data = {
    "gender": "male" if gender == 1 else "female",
    "age_group": age_group,
    "casual_wear": {
        "shirts": shirts,
        "trousers": trousers
    },
    "occasional_wear": occasional_wear
}

# Save or update the main JSON file
all_users[name] = user_data
with open("users_data.json", "w") as file:
    json.dump(all_users, file, indent=4)

print(f"Data for {name} saved successfully!")
    

        
