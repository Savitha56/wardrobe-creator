import json

# Example dictionary
data = {"name": "Dharaneeshwaran", "age": 20, "city": "Coimbatore"}

# Writing dictionary to a file
with open("data.json", "w") as file:
    json.dump(data, file)  # store dictionary as JSON

# Reading dictionary from the file
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)




if n==1:
        dress=int(input("you need store your \n1.shirt \n2.pant "))
        
        if dress==1:
            user_dict = {}
            num_items = int(input("how many shirts do you have ?"))
            for i in range(num_items):
                key = input(f"Enter the shirt number: ")
                value = input(f"Enter the colour of the shirt : ")
                user_dict[key] = value   
            with open("user_dict.json", "w") as file:
                json.dump(user_dict, file) 
            with open("user_dict.json", "r") as file:
                loaded_data = json.load(file)
            print(loaded_data)

        if dress==2:
            user = {}
            num = int(input("how many pants do you have ?"))
            for i in range(num):
                key = input(f"Enter the pant number: ")
                value = input(f"Enter the colour of the pant : ")
                user[key] = value
    
    with open("user_dict.json", "w") as file:
        json.dump(user_dict, file) 
    with open("user_dict.json", "r") as file:
        loaded_data = json.load(file)
    print(loaded_data)
    with open("user.json", "w") as file:
        json.dump(user, file) 
    with open("user.json", "r") as file:
        loaded = json.load(file)
    print(loaded)

        
