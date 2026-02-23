hero_0 = {
    "name": "superman",
    "power": "super strength", 
    "strength": 100,
}

hero_1 = {
    "name": "batman",
    "power": "intellect", 
    "strength": 85,
    "speed": 80
}
hero_list = [hero_0, hero_1]
print (hero_list)

if "name" in hero_0:
    print("The superhero's name is:", hero_0["name"])
else:
    print("There is no superhero name.")

if "power" in hero_0:
    print("The superhero's power is:", hero_0["power"])
else:
    print("There is no superhero power.")

if "strength" in hero_0:
    print("The superhero's strength is:", hero_0["strength"])
else:
    print("There is no superhero strength.")

print(hero_0)

hero_0["speed"] = 120
print(hero_0)

hero_0["strength"] = 100
print(hero_0)

print("Superhero 1 stats \n")
for i in hero_0:
    print(i, ":", hero_0[i])

print("Superhero 2 stats \n")
for i in hero_1:
    print(i, ":", hero_1[i])

for i in hero_list:
    print(i["name"] + "'s superpower is", i["power"], "and their strength value is", i["strength"])
