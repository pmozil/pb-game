import game_orig

kozelnytska = game_orig.Street("Kozelnytska")
kozelnytska.set_description("A nice, clean street")
wallet = game_orig.Item("wallet")
wallet.set_description("Gotta have some money around here")
kozelnytska.set_item(wallet)

franka = game_orig.Street("Franka street")
kozelnytska.set_description("So... long...")
cigs = game_orig.Item("cigarette")
cigs.set_description("Maybe you should not have picked it up?")
franka.set_item(cigs)
lotr = game_orig.Lotr()
franka.set_character(lotr)

shevch = game_orig.Street("Shevchenka")
shevch.set_description("Ooh, an opera!")
batyar = game_orig.Batyar()
shevch.set_character(batyar)

krak = game_orig.Street("Krakivska")
krak.set_description("Finally, now for the track back")
wallet = game_orig.Item("wallet")
wallet.set_description("Gotta have some money around here")
kozelnytska.set_item(wallet)

kozelnytska.link_room(franka, "south")
franka.link_room(kozelnytska, "north")

franka.link_room(shevch, "west")
shevch.link_room(franka, "east")

shevch.link_room(krak, "north")
krak.link_room(shevch, "south")

current_room = kozelnytska

backpack = []

dead = False

while dead == False:
    print("\n")
    enemy_dealt_with = False
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if (
        command in ["north", "south", "east", "west"]
        and current_room.character is None
    ):
        # Move in the given direction
        current_room = current_room.move(command)
    if (
        command in ["north", "south", "east", "west"]
        and not current_room.character is not None
    ):
        print("Deal with the person first, you rude harlot!")
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
            # Fight with the inhabitant, if there is one
            print("What will you deal with the person with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost.")
                    print("That's the end of the game.")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to deal with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)
