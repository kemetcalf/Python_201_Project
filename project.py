import requests

pokemon_target = input(
    "Please enter the name of the Pokemon you wish to find: ")
pokemon_target = pokemon_target.lower()
throw_pokeball = requests.get(
    f"https://pokeapi.co/api/v2/pokemon/{pokemon_target}")

if throw_pokeball.status_code == 200:
    my_pokemon = throw_pokeball.json()
    print(f"I choose you, {my_pokemon['name'].capitalize()}!")
    for type_dict in my_pokemon["types"]:
        print(f"{type_dict['type']['name'].capitalize()} type Pokemon")
    print("Abilities: ")
    for ability_dict in my_pokemon["abilities"]:
        print(f"\t{ability_dict['ability']['name'].capitalize()}")
else:
    print("No such Pokemon :(")
