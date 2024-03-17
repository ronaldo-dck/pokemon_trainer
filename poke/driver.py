# driver.py
import sys
from pyke import knowledge_engine
from pyke import krb_traceback
from pyke import goal

engine = knowledge_engine.engine(__file__)
goal_get_pokemon = goal.compile('moves.get_pokemon($pokemon_name, $move_name, $attack_strategy, $attack_type)')
goal_get_type = goal.compile('pk_types.type_name($type_id, $pokemon_name)')

def best_against(element1, element2='null'):

    engine.reset()
    engine.activate('backward')
    try:
        vars, plan = engine.prove_1_goal('backward.most_effective($attacker1, $attacked1, $attacked2)', attacked1=element1, attacked2=element2)
        # print("%s is the best against %s and %s" % (vars['attacker1'], element1, element2))
        return vars['attacker1']
    except:
        print('não foi possível')

    print()


def attack_strategy(ph_defense = 1, sp_defense = 1) :

    engine.reset()
    engine.activate('backward')
    try:
        vars, plan = engine.prove_1_goal('backward.attack_strategy($attack_type, $ph_defense, $sp_defense)', ph_defense=ph_defense, sp_defense=sp_defense)
        # print("%s is the best attack strategy" % (vars['attack_type']))
        return vars['attack_type']
    except:
        print('não foi possível')

def get_pokemon(attack_strategy, attack_type):

    engine.reset()
    engine.activate('forward')
    with goal_get_pokemon.prove(engine, attack_strategy=attack_strategy, attack_type=attack_type) as gen:
        for vars, plan in gen:
            # print("%s attacks with %s" % (vars['pokemon_name'], vars['move_name']))
            return vars

def get_type(type_id):

    engine.reset()
    engine.activate('forward')
    with goal_get_type.prove(engine, type_id=type_id) as gen:
        for vars, plan in gen:
            # print("%s id name is %s" % (type_id, vars['pokemon_name']))
            return vars['pokemon_name']