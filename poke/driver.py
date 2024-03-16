# driver.py
import sys
from pyke import knowledge_engine
from pyke import krb_traceback
from pyke import goal

engine = knowledge_engine.engine(__file__)

def best_against(element1='fire', element2='null'):

    engine.reset()
    engine.activate('backward')
    try:
        vars, plan = engine.prove_1_goal('backward.most_effective($attacker1, $attacked1, $attacked2)', attacked1=element1, attacked2=element2)
        print("%s is the best against %s and %s" % (vars['attacker1'], element1, element2))
    except:
        print('não foi possível')

    print()


