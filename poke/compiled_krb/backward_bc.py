# backward_bc.py

from pyke import contexts, pattern, bc_rule

pyke_version = '1.1.1'
compiler_version = 1

def check_weakness_x4(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if context.lookup_data('attacked1') != context.lookup_data('attacked2'):
          if context.lookup_data('attacked2') != 'null':
            with engine.prove('pk_types', 'super_effective', context,
                              (rule.pattern(0),
                               rule.pattern(1),)) \
              as gen_3:
              for x_3 in gen_3:
                assert x_3 is None, \
                  "backward.check_weakness_x4: got unexpected plan from when clause 3"
                with engine.prove('pk_types', 'super_effective', context,
                                  (rule.pattern(0),
                                   rule.pattern(2),)) \
                  as gen_4:
                  for x_4 in gen_4:
                    assert x_4 is None, \
                      "backward.check_weakness_x4: got unexpected plan from when clause 4"
                    rule.rule_base.num_bc_rule_successes += 1
                    yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def check_weakness_x2(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if context.lookup_data('attacked1') != context.lookup_data('attacked2'):
          with engine.prove('pk_types', 'super_effective', context,
                            (rule.pattern(0),
                             rule.pattern(1),)) \
            as gen_2:
            for x_2 in gen_2:
              assert x_2 is None, \
                "backward.check_weakness_x2: got unexpected plan from when clause 2"
              rule.rule_base.num_bc_rule_successes += 1
              yield
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def get_attack_strategy_special(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if context.lookup_data('ph_defense') >= context.lookup_data('sp_defense'):
          mark2 = context.mark(True)
          if rule.pattern(0).match_data(context, context,
                  'special'):
            context.end_save_all_undo()
            rule.rule_base.num_bc_rule_successes += 1
            yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def get_attack_strategy_physical(rule, arg_patterns, arg_context):
  engine = rule.rule_base.engine
  patterns = rule.goal_arg_patterns()
  if len(arg_patterns) == len(patterns):
    context = contexts.bc_context(rule)
    try:
      if all(map(lambda pat, arg:
                   pat.match_pattern(context, context,
                                     arg, arg_context),
                 patterns,
                 arg_patterns)):
        rule.rule_base.num_bc_rules_matched += 1
        if context.lookup_data('ph_defense') < context.lookup_data('sp_defense'):
          mark2 = context.mark(True)
          if rule.pattern(0).match_data(context, context,
                  'physical'):
            context.end_save_all_undo()
            rule.rule_base.num_bc_rule_successes += 1
            yield
          else: context.end_save_all_undo()
          context.undo_to_mark(mark2)
        rule.rule_base.num_bc_rule_failures += 1
    finally:
      context.done()

def populate(engine):
  This_rule_base = engine.get_create('backward')
  
  bc_rule.bc_rule('check_weakness_x4', This_rule_base, 'most_effective',
                  check_weakness_x4, None,
                  (contexts.variable('attacker1'),
                   contexts.variable('attacked1'),
                   contexts.variable('attacked2'),),
                  (),
                  (contexts.variable('attacker1'),
                   contexts.variable('attacked1'),
                   contexts.variable('attacked2'),))
  
  bc_rule.bc_rule('check_weakness_x2', This_rule_base, 'most_effective',
                  check_weakness_x2, None,
                  (contexts.variable('attacker1'),
                   contexts.variable('attacked1'),
                   contexts.variable('attacked2'),),
                  (),
                  (contexts.variable('attacker1'),
                   contexts.variable('attacked1'),))
  
  bc_rule.bc_rule('get_attack_strategy_special', This_rule_base, 'attack_strategy',
                  get_attack_strategy_special, None,
                  (contexts.variable('attack_type'),
                   contexts.variable('ph_defense'),
                   contexts.variable('sp_defense'),),
                  (),
                  (contexts.variable('attack_type'),))
  
  bc_rule.bc_rule('get_attack_strategy_physical', This_rule_base, 'attack_strategy',
                  get_attack_strategy_physical, None,
                  (contexts.variable('attack_type'),
                   contexts.variable('ph_defense'),
                   contexts.variable('sp_defense'),),
                  (),
                  (contexts.variable('attack_type'),))


Krb_filename = '../backward.krb'
Krb_lineno_map = (
    ((14, 18), (2, 2)),
    ((20, 20), (4, 4)),
    ((21, 21), (5, 5)),
    ((22, 28), (7, 7)),
    ((29, 35), (8, 8)),
    ((48, 52), (11, 11)),
    ((54, 54), (13, 13)),
    ((55, 61), (15, 15)),
    ((74, 78), (18, 18)),
    ((80, 80), (20, 20)),
    ((83, 83), (21, 21)),
    ((99, 103), (24, 24)),
    ((105, 105), (26, 26)),
    ((108, 108), (27, 27)),
)
