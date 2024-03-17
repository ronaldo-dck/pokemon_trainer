# forward_fc.py

from pyke import contexts, pattern, fc_rule, knowledge_base

pyke_version = '1.1.1'
compiler_version = 1

def get_pokemon(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('moves', 'poke_moves', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('moves', 'get_pokemon',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),
                        rule.pattern(2).as_data(context),
                        rule.pattern(3).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def get_type(rule, context = None, index = None):
  engine = rule.rule_base.engine
  if context is None: context = contexts.simple_context()
  try:
    with knowledge_base.Gen_once if index == 0 \
             else engine.lookup('pk_types', 'type_id', context,
                                rule.foreach_patterns(0)) \
      as gen_0:
      for dummy in gen_0:
        engine.assert_('pk_types', 'type_name',
                       (rule.pattern(0).as_data(context),
                        rule.pattern(1).as_data(context),)),
        rule.rule_base.num_fc_rules_triggered += 1
  finally:
    context.done()

def populate(engine):
  This_rule_base = engine.get_create('forward')
  
  fc_rule.fc_rule('get_pokemon', This_rule_base, get_pokemon,
    (('moves', 'poke_moves',
      (contexts.variable('pokemon_name'),
       contexts.variable('move_name'),
       contexts.variable('attack_strategy'),
       contexts.variable('attack_type'),),
      False),),
    (contexts.variable('pokemon_name'),
     contexts.variable('move_name'),
     contexts.variable('attack_strategy'),
     contexts.variable('attack_type'),))
  
  fc_rule.fc_rule('get_type', This_rule_base, get_type,
    (('pk_types', 'type_id',
      (contexts.variable('type_id'),
       contexts.variable('pokemon_name'),),
      False),),
    (contexts.variable('type_id'),
     contexts.variable('pokemon_name'),))


Krb_filename = '../forward.krb'
Krb_lineno_map = (
    ((12, 16), (3, 3)),
    ((17, 21), (5, 5)),
    ((30, 34), (9, 9)),
    ((35, 37), (11, 11)),
)
