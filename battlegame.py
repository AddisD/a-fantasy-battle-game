wizard = "Wizard"
elf = "Elf"
human = "Human"
wizard_hp = 70
elf_hp = 100
human_hp = 150
wizard_damage = 150
elf_damage = 100
human_damage = 20
dragon_damage = 50
dragon_hp = 300
character = 0
print("""
1) Wizard
2)Elf
3)Human
""")
character = input("Choose your character: ")
while True:
    if character == "1":
        print(
            f"you have choosen: {wizard}\nHealth=   {wizard_hp}\nDamage= {wizard_damage}")
        break
    elif character == "2":
        print(
            f"you have choosen:  {elf}\nHealth= {elf_hp}\nDamage= {elf_damage}")
        break
    elif character == "3":
        print(
            f"you have choosen:   {human}\nHealth= {human_hp}\nDamage= {human_damage}")
        break
    else:
        print("Unknown character.")
        break
while True:
    if character == "1":
        dragon_hp = dragon_hp-wizard_damage
        wizard_hp = wizard_hp-dragon_damage
        print(
            f"The {wizard} damaged the Dragon!\nThe Dragon's hitpoints are now: {dragon_hp}")

        if dragon_hp <= 0:
            print(f"The Dragon has lost the battle.")
            break
        print(
            f"The Dragon strikes back at {wizard}\nThe {wizard} hitpoints are now: {wizard_hp}")
        if wizard_hp <= 0:
            print(f"The wizard has lost the battle.")
            break
    elif character == "2":
        dragon_hp = dragon_hp - elf_damage
        elf_hp = elf_hp-dragon_damage
        print(
            f"The {elf} damaged the Dragon!\nThe Dragon's hitpoints are now: {dragon_hp}")
        if dragon_hp <= 0:
            print(f"The Dragon has lost the battle.")
            break
        print(
            f"The Dragon strikes back at {elf}\nThe {elf} hitpoints are now: {elf_hp}")
        if elf_hp <= 0:
            print(f"The {elf} has lost the battle.")
            break
    elif character == "3":
        dragon_hp = dragon_hp - human_damage
        human_hp = human_hp-dragon_damage
        print(
            f"The {human} damaged the Dragon!\nThe Dragon's hitpoints are now: {dragon_hp}")
        if dragon_hp <= 0:
            print(f"The Dragon has lost the battle.")
            break
        print(
            f"The Dragon strikes back at {human}\nThe {human} hitpoints are now: {human_hp}")
        if human_hp <= 0:
            print(f"The {human} has lost the battle.")
            break
