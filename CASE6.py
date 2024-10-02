#Case 6:Dictionary application: promotion and salary increase

info_dict = {
    "u\'s":{
        "Department": "Science",
        "wage": 3000,
        "Level": 1
    },
    "Aqours":{
        "Department": "Marketing",
        "wage": 5000,
        "Level": 2
    },
    "Nijigasaki":{
        "Department": "Marketing",
        "wage": 7000,
        "Level": 3
    },
    "Liella":{
        "Department": "Science",
        "wage": 4000,
        "Level": 1
    },
    "Hosunosora":{
        "Department": "Marketing",
        "wage": 6000,
        "Level": 2
    }

}

print(f"The results of employees before promotion and salary increase:{info_dict}")

#for loop
for name in info_dict:
    if info_dict[name]["Level"] == 1:
        employee_info_dict = info_dict[name]
        employee_info_dict["Level"] = 2
        employee_info_dict["wage"] += 1000
        info_dict[name] = employee_info_dict

print(f"The results of employees after promotion and salary increase: {info_dict}")