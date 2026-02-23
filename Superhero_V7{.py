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