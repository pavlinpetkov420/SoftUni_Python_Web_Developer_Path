from guild.project import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon_name: Pokemon):
        is_added = [p for p in self.pokemons if p == pokemon_name]
        if is_added:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon_name)
        return f"Caught {Pokemon.pokemon_details(pokemon_name)}"

    def release_pokemon(self, pokemon_name: str):
        is_added = [p for p in self.pokemons if p == pokemon_name]
        if not is_added:
            return "Pokemon is not caught"
        self.pokemons.remove(pokemon)
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        trainer_info = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for p in self.pokemons:
            trainer_info += f"- {Pokemon.pokemon_details(p)}\n"
        return trainer_info


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
