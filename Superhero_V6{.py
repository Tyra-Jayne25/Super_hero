hero_0 = {
    "Name": "superman",
    "Power": "super strength", 
    "Strength": 100,
}

hero_1 = {
    "Name": "batman",
    "Power": "intellect", 
    "Strength": 85,
    "Speed": 80
}

hero_list = [hero_0, hero_1]
print (hero_list)

if "Name" in hero_0:
    print("The superhero's name is:", hero_0["Name"])
else:
    print("There is no superhero name.")

if "Power" in hero_0:
    print("The superhero's power is:", hero_0["Power"])
else:
    print("There is no superhero power.")

if "Strength" in hero_0:
    print("The superhero's strength is:", hero_0["Strength"])
else:
    print("There is no superhero strength.")

print(hero_0)

hero_0["speed"] = 120
print(hero_0)

hero_0["Strength"] = 100
print(hero_0)

popped_item = hero_0.pop("Power")
print(hero_0)
print(popped_item)

print("Superhero 1 stats \n")
for i in hero_0:
    print(i, ":", hero_0[i])


