# driver.py
import sys
from pyke import knowledge_engine
from pyke import krb_traceback
from pyke import goal

engine = knowledge_engine.engine(__file__)

fc_goal = goal.compile('elements.not_recomended($element1, $element2)')

def is_effective_fc(element1='fire'):

    engine.reset()

    engine.activate('forward')
    with fc_goal.prove(engine, element1=element1) as gen:
        for vars, plan in gen:
            print("%s is not recomended against %s" % (element1, vars['element2']))

def is_effective_bc(element1='fire'):

    engine.reset()

    engine.activate('backward')
    with engine.prove_goal('backward.not_recomended($element1, $element2)', element1=element1) as gen:
        for vars, plan in gen:
            print("%s is not recomended against %s" % (element1, vars['element2']))
