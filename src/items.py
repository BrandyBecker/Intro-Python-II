class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}, {self.description}"

    def on_pickup(self):
        print(f"You picked up the {self.name}.")

    def on_drop(self):
        print(f"You drop your {self.name}.")