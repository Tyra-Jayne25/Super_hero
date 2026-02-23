heroes = {"SUP":
          {"name": "superman",
           "power": "super strength",
           "strength": 100,
           "speed": 120},
           "BAT":
           {"name": "batman",
            "power": "intellect",
            "strength": 85,
            "speed": 80}
}

for hero_id, hero_info in heroes.items():
    print("\nHero ID:", hero_id)

    for key in hero_info:
        print(key + ":", hero_info[key])

heroes = {}

for i in range(2):
    ID = input("\n\nEnter ID: ")
    heroes[ID] = {}

    name = input("Enter name: ")
    heroes[ID] ["name"] = name

    power = input("Enter power: ")
    heroes[ID] ["power"] = power

    strength = int(input("Enter strength: "))
    heroes[ID] ["strength"] = strength

    speed = int(input("Enter speed: "))
    heroes[ID] ["speed"] = speed

    print("\n\n")
    print(heroes)