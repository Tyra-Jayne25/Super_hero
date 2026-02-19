hero_0 = {
    "name": "superman",
    "Power": "super strength", 
    "Strength": 100
}

print(hero_0["name"])
print(hero_0["Power"])
print(hero_0["Strength"])

if "name" in hero_0:
    print("The superhero's name is:", hero_0["name"])
else:
    print("There is no superhero name.")

if "Power" in hero_0:
    print("The superhero's power is:", hero_0["Power"])
else:
    print("There is no superhero power.")

if "superman" in hero_0["name"]:
    print("That is the superhero's name.")
else:
    print("That isn't the superhero's name.")

if "kryptonite" in hero_0["name"]:
    print("That is the superhero's name.")
else:
    print("That isn't the superhero's name.")