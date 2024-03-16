# forward_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def unrecomendations(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('elements', 'super_effective', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('elements', 'not_recomended',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def defense_set(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('elements', 'attack_effective', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('elements', 'attack_recomended',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def get_name(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('elements', 'pokemon', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        print(context.lookup_data('tipo1'))
        engine.assert_('elements', 'result',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('forward')
  
  fc_rule.fc_rule('unrecomendations', This_rule_base, unrecomendations,
    (('elements', 'super_effective',
      (contexts.variable('elementAtk'),
       contexts.variable('elementDfs'),),
      False),),
    (contexts.variable('elementAtk'),
     contexts.variable('elementDfs'),))
  
  fc_rule.fc_rule('defense_set', This_rule_base, defense_set,
    (('elements', 'attack_effective',
      (contexts.variable('atk'),
       contexts.variable('dfs'),),
      False),),
    (contexts.variable('atk'),
     contexts.variable('dfs'),))
  
  fc_rule.fc_rule('get_name', This_rule_base, get_name,
    (('elements', 'pokemon',
      (contexts.variable('nome'),
       contexts.variable('tipo1'),
       contexts.variable('tipo2'),),
      False),),
    (contexts.variable('nome'),
     contexts.variable('tipo1'),
     contexts.variable('tipo2'),))


Krb_filename = '../forward.krb'
Krb_lineno_map = (
    ((12, 16), (3, 3)),
    ((17, 19), (5, 5)),
    ((28, 32), (9, 9)),
    ((33, 35), (11, 11)),
    ((44, 48), (15, 15)),
    ((49, 49), (17, 17)),
    ((50, 53), (18, 18)),
)
