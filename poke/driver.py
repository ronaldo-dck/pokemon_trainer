# driver.py
import sys
from pyke import knowledge_engine
from pyke import krb_traceback
from pyke import goal

engine = knowledge_engine.engine(__file__)

fc_goal = goal.compile('elements.not_recomended($elementAtk, $elementDfs)')
attack_goal = goal.compile('elements.attack_recomended($atk, $dfs)')
general_goal = goal.compile('elements.recomended($element, $atk)')
pokemon_goal = goal.compile('elements.result($nome, $tipo1, $tipo2)')

# get_infos(OP)
# 

def is_effective_fc(element1='fire'):

    engine.reset()

    engine.activate('forward')
    with fc_goal.prove(engine, elementAtk=element1) as gen:
        for vars, plan in gen:
            print("%s is not recomended against %s" % (element1, vars['elementDfs']))


def nameLegal(dfs ='defense'):
    engine.reset()
    engine.activate('forward')
    with attack_goal.prove(engine, dfs=dfs) as gen:
        for vars, plan in gen:
            print("%s recomended against %s" % (vars['dfs'], vars['atk']))


def getPokemon(name='bubassauro'):
    engine.reset()
    engine.activate('forward')
    with pokemon_goal.prove(engine, nome=name) as gen:
        for vars, plan in gen:
            print("%s tipo1 %s tipo2 %s" % (name, vars['tipo1'], vars['tipo2']))



def is_effective_bc(element1='fire'):

    engine.reset()
    engine.activate('backward')
    with engine.prove_goal('backward.not_recomended($element1, $element2)', element1=element1) as gen:
        for vars, plan in gen:
            print("%s is not recomended against %s" % (element1, vars['element2']))


