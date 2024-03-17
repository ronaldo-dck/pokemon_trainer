import driver
import pandas as pd

pokemons = pd.read_csv('../pokemon.csv')
pokemon_types = pd.read_csv('../pokemon_types.csv')
pokemon_stats = pd.read_csv('../pokemon_stats.csv')


def get_pokemon(id=1):
    value = f'{id}'
    if value.isnumeric():
        oponente = pokemons[pokemons['id'] == int(value)]
    else:
        oponente = pokemons[pokemons['identifier'] == value]

    if len(oponente) == 0:
        oponente = get_pokemon()

    return (oponente.iloc[0]['identifier'], oponente.iloc[0]['id'])

def get_defense_stats(index):
    oponente_stats = pokemon_stats[pokemon_stats['pokemon_id'] == index]

    id_defense = 3
    id_sp_defense = 5

    return (
        oponente_stats[oponente_stats['stat_id'] == id_defense].iloc[0]['base_stat'],
        oponente_stats[oponente_stats['stat_id'] == id_sp_defense].iloc[0]['base_stat']
    )


def build_pokemon(id):
    types_oponente = pokemon_types[pokemon_types['pokemon_id'] == id]['type_id'].values
    
    stats = get_defense_stats(id)

    return ( types_oponente, stats)

def get_pokemon_type(type1, type2):
    return driver.best_against(type1, type2)

def translate_pokemon_type(id):
    return driver.get_type(id)

def get_attack(defense, sp_defense):
    return driver.attack_strategy(defense, sp_defense)

def get_recommended_pokemon(attack, type):
    return driver.get_pokemon(attack, type)



if __name__ == '__main__':
        name, id = get_pokemon((input('Entre como ID')))
        types, stats = build_pokemon(id)

        type1 = translate_pokemon_type(types[0])
        type2 = 'null'
        if len(types) == 2:
            type2 = translate_pokemon_type(types[1])

        bestType = get_pokemon_type(type1, type2)
        bestAttack = get_attack(stats[0], stats[1])

        print(f'oponente: {name} {type1} {type2} buscando por: {bestType} {bestAttack}')
        recommended = get_recommended_pokemon(bestAttack, bestType)

        print('player', recommended['pokemon_name'], recommended['move_name'])

