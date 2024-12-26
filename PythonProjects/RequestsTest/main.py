import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e14616c748091211ca1cd05e393fc2e5'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}

body_create = {
    "name": "generate",
    "photo_id": 150
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.status_code, response_create.text)'''

body_change = {
    "pokemon_id": "171573",
    "name": "Pikachu",
    "photo_id": 150
}

'''response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_create.status_code, response_create.text)'''

body_catch = {
    "pokemon_id": "171573"
}

'''response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_create.status_code, response_create.text)'''