class Pokemon:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp

    def pokemon_details(self):
        return f"{self.name} with health {self.hp}"
