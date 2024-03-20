from poke import driver
import pandas as pd
from colorama import Fore, Style


RED='\033[0;31m'
HEADER='\033[95m'
OKBLUE='\033[94m'
OKGREEN='\033[92m'
WARNING='\033[93m'
FAIL='\033[91m'
BOLD='\033[1m'
UNDERLINE='\033[4m'
ENDC='\033[0m'

pokemons = pd.read_csv('data/pokemon.csv')
pokemon_types = pd.read_csv('data/pokemon_types.csv')
pokemon_stats = pd.read_csv('data/pokemon_stats.csv')


def get_pokemon():
    value = (input('Number/id do pokemon: ')).lower()

    if value.isnumeric():
        oponente = pokemons[pokemons['id'] == int(value)]
    else:
        oponente = pokemons[pokemons['identifier'] == value]

    if len(oponente) == 0:
        print("id/name errado -> EXIT")   
        exit(2)
        

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

    recommended = driver.get_pokemon(attack, type)
    recommended['pokemon_name'] = str(recommended['pokemon_name']).capitalize()
    recommended['move_name'] = str(recommended['move_name']).capitalize()
    return recommended


if __name__ == '__main__':
        name, id = get_pokemon()
        types, stats = build_pokemon(id)

        type1 = translate_pokemon_type(types[0])
        type2 = 'null' if len(types) == 1 else translate_pokemon_type(types[1])

        bestType = get_pokemon_type(type1, type2)
        bestAttack = get_attack(stats[0], stats[1])

        recommended = get_recommended_pokemon(bestAttack, bestType)
        
        name = str(name).capitalize()
        type1 = str(type1).capitalize()
        type2 = str(type2).capitalize() if type2 != 'null' else ''
        bestType = str(bestType).capitalize()
        bestAttack = str(bestAttack).capitalize()

        print(f'Oponente: {Fore.BLUE}{name}{Style.RESET_ALL}  Types[{Fore.GREEN}{type1}{Style.RESET_ALL} {Fore.GREEN}{type2}{Style.RESET_ALL}]')
        print(f'Buscando por um golpe do tipo: {Fore.RED}{bestType}{Style.RESET_ALL} que cause dano {Fore.YELLOW}{bestAttack}{Style.RESET_ALL}')
        print('Use o Pokemon', Fore.BLUE + recommended['pokemon_name'] + Style.RESET_ALL, 'aplicando o golpe', Fore.RED + recommended['move_name'] + Style.RESET_ALL)
        