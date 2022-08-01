number_of_heroes = int(input())

heroes = {}

for hero in range(number_of_heroes):
    heroes_input = input().split(' ')
    heroes[heroes_input[0]] = {"hp": int(heroes_input[1]), "mana": int(heroes_input[2])}

while True:
    commands = input().split(' - ')
    if commands[0] == 'End':
        break

    if commands[0] == 'CastSpell':
        name = commands[1]
        mp_needed = int(commands[2])
        spell_name = commands[3]
        if mp_needed <= heroes[name]["mana"]:
            heroes[name]["mana"] -= mp_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['mana']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif commands[0] == "TakeDamage":
        hero_name = commands[1]
        damage = int(commands[2])
        attacker = commands[3]
        if damage < heroes[hero_name]["hp"]:
            heroes[hero_name]["hp"] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['hp']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]

    elif commands[0] == "Recharge":
        hero_name = commands[1]
        amount = int(commands[2])
        heroes[hero_name]["mana"] += amount
        mana_recharged = amount
        if heroes[hero_name]["mana"] > 200:
            mana_recharged = heroes[hero_name]["mana"] - (200 + amount)
            heroes[hero_name]["mana"] = 200
        print(f"{hero_name} recharged for {abs(mana_recharged)} MP!")

    elif commands[0] == "Heal":
        hero_name = commands[1]
        amount = int(commands[2])
        heroes[hero_name]["hp"] += amount
        heroes_healed = amount

        if heroes[hero_name]["hp"] > 100:
            heroes_healed = heroes[hero_name]["hp"] - (100 + amount)
            heroes[hero_name]["hp"] = 100
        print(f"{hero_name} healed for {abs(heroes_healed)} HP!")


for hero in heroes:
    print(hero)
    print(f"  HP: {heroes[hero]['hp']}")
    print(f"  MP: {heroes[hero]['mana']}")