"""The game module"""


class Street:
    """The room class"""

    def __init__(self, name: str):
        """Init for room"""
        self.name = name
        self.directions: dict[str, "Street"] = {}
        self.description: str = "A weirdly uncharacteristic room.\
You feel like it doesn't exist."
        self.character: "Enemy | None" = None
        self.item: "Item | None" = None

    def link_room(self, room: "Street", direction: str):
        """Link the room"""
        self.directions[direction] = room

    def set_description(self, description: str):
        """Set description for the game"""
        self.description = description

    def set_character(self, char: "Enemy"):
        """set character"""
        self.character = char

    def set_item(self, item: "Item | None"):
        """Set the item"""
        self.item = item

    def get_item(self) -> "Item | None":
        """Get the item"""
        return self.item

    def get_character(self) -> "Enemy | None":
        """Get the character"""
        return self.character

    def move(self, direction: str) -> "Street":
        """Move to another room"""
        return self.directions[direction]

    def get_details(self):
        """Describe room"""
        print(self.name)
        print("-" * 30)
        print(self.description)
        for key, val in self.directions.items():
            print(f"The {val.name} is {key}")


class Enemy:
    """The enemy class"""

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.converastion = "Who... am I?"
        self.weakness: str | None = None

    def describe(self):
        """Describe inhabitant"""
        print(self.description)

    def set_conversation(self, convo: str):
        """Set the caracter's conversation line"""
        self.converastion = convo

    def set_weakness(self, weak: str):
        """Set the character's weakness"""
        self.weakness = weak

    def talk(self):
        """Talk with the enemy"""
        print(self.converastion)

    def fight(self, item: str) -> bool:
        """Check if character is weak to the item"""
        if self.weakness is None:
            return False
        return item == self.weakness


class Batyar(Enemy):
    """The abtyar class"""

    def __init__(self):
        super().__init__(
            "A nice old batyar",
            "This guy is dressed surprisingly well for how he behaves",
        )
        self.set_conversation("Hey, wanna go get a drink?")

    def fight(self, item: str) -> bool:
        inp = input("Do you go for a drink?")
        return inp.lower().startswith("y") and item == "wallet"


class Lotr(Enemy):
    """The abtyar class"""

    def __init__(self):
        super().__init__(
            "A scary looking bozo",
            "Why is he so... Tiny?",
        )
        self.set_conversation("May i borrow a cigarette?")
        self.set_weakness("cigarette")


class Cavalier(Enemy):
    """The cavalier class"""

    def __init__(self):
        super().__init__(
            "A guy with a rose",
            "He looks like he would cry if you looked at him wrong",
        )
        self.set_conversation("Lemme get you a beer!")

    def fight(self, item: str) -> bool:
        inp = input("Do you go for a beer?")
        if inp.lower.startswith("y"):
            print("You died")
            return False
        print("The cavalier screams like a baby and runs away")
        return True


class Item:
    """The item class"""

    def __init__(self, name: str):
        """Init for the Item"""
        self.name = name
        self.description: str = "À̸̛̛̠͕̲͎̻̺̹͕͕̤̰̟̫̺̙́̄̓̈́̈́̅͒͊͐̃͗̀͛̇͊͌̉̊̉̽͂̕̕͜ ̴̧̣̮̠͓̠͇̙̟͍̳͓̙͈͈̥̤̈͂͛̆̈̕͠w̷̨̨̡̨̪̫̠̗̟̣͉̜͚̖̻̼̝̙͕̺̱͕̤̗̠̣̎̔̃̏̃̍̀̎̊̓̋̉͛͐́͑̉̏̿̕͘̕͜͜͠ó̵̥̪̳͔͍͍̱̣̰͚̩̬̺͔̺̮̟̜͓̪̥̼̪̪̈͗̋̊͐̚͜͜ͅn̵̢̢̡̧̤̜͓͍̫̬͖̲̖̘̯̤̝̿̈́̓̿͐̒̀̈̄̀̃̈̑̀͌͌̔͊̂̅͒̿̕̕̚͜͠͝k̴̛̻̞̀͂͒͋̅͌͛̃̔̇̔͛̐͌̆̚͠͝y̸̧̛̻̖̳̹͕̣̩̼̰̺̦̭̱͉̩͇̗͓̬̫̩̳̯̗̆̾̈̂̈̊̓̌̿͊̓͂͊̆̓́͑̀̚͘͜͠͝ ̶̧̧̢͇̲͖̰͕̮̣̪̻̱̼̹̤̞̼̰͖̞̜͖͕̈̓̆̏̀͌̔̍͐̔͒͌̉̀̉̀̌͆͂̈́͌̉̿̔̎͘͜͝ͅs̵̡̟͇̺͚͍̦̈̊̅̂͛̕ṱ̸͖͕̇͂̂̽͆̒̎͌͌͛̿͒͐͑̈̑̄͗̀́̕̕̚̚ĭ̵̢̗̯͓̙͔͒͌̓̌̒̆̒̈͗̌̆̓͛̋̌͗̕͝͠͝ͅç̵̌̍͐̽̋͊͒̋̆͑͊͆̀̕͠k̴̨͈̤̝̘͙̩̞̬̯̭̬̖̰̺̪̆"

    def get_name(self) -> str:
        """Get the item's name"""
        return self.name

    def describe(self):
        """Get the item's description"""
        print(self.description)

    def set_description(self, descr: str):
        """Set the item's description"""
        self.description = descr
