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

def populate(engine):
  This_rule_base = engine.get_create('forward')
  
  fc_rule.fc_rule('unrecomendations', This_rule_base, unrecomendations,
    (('elements', 'super_effective',
      (contexts.variable('element1'),
       contexts.variable('element2'),),
      False),),
    (contexts.variable('element2'),
     contexts.variable('element1'),))


Krb_filename = '../forward.krb'
Krb_lineno_map = (
    ((12, 16), (3, 3)),
    ((17, 19), (5, 5)),
)
