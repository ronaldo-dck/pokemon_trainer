# driver.py
import sys
from pyke import knowledge_engine
from pyke import krb_traceback
from pyke import goal

engine = knowledge_engine.engine(__file__)

def best_against(element1='fire', element2='null'):

    engine.reset()

    engine.activate('backward')
    with engine.prove_goal('backward.most_effective($attacker1, $attacker2, $attacked1, $attacked2)', attacked1=element1, attacked2=element2) as gen:
        for vars, plan in gen:
            print("%s and %s is the best against %s and %s" % (vars['attacker1'], vars['attacker2'], element1, element2))

    print()
