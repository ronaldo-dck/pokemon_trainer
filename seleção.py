import pandas as pd
from tqdm import tqdm




dados_escolhidos = []
# Assuming your loop iterates over a range of indices
# for index in tqdm(range(1, 1026), desc="Processing"):
#     moves = pd.read_csv('moves.csv')
#     pokemon_moves = pd.read_csv('pokemon_moves.csv')
#     pokemon_stats = pd.read_csv('pokemon_stats.csv')
#     pokemon_types = pd.read_csv('pokemon_types.csv')
#     pokemon = pd.read_csv('pokemon.csv')
#     stats = pd.read_csv('stats.csv')
#     type_efficacy = pd.read_csv('type_efficacy.csv')
#     types = pd.read_csv('types.csv')


# # Types 
# # 


#     oponente = pokemon[pokemon['id'] == index]

#     #DEFINIDO O TIPO MAIS EFICAZ CONTRA O OPNENTE
#     types_oponente = pokemon_types[pokemon_types['pokemon_id']
#                                 == index]['type_id'].values

#     if len(types_oponente) > 1:
#         # Se houver dois tipos de ataque eficazes contra o oponente
#         types_ataque = type_efficacy[(type_efficacy['target_type_id'] == types_oponente[0]) | (
#             type_efficacy['target_type_id'] == types_oponente[1])]
#     else:
#         # Se houver apenas um tipo de ataque eficaz contra o oponente
#         types_ataque = type_efficacy[type_efficacy['target_type_id'] == types_oponente[0]]

#     types_ataque = types_ataque[types_ataque['damage_factor'] == 200]
#     count_targets = types_ataque.groupby('damage_type_id')['target_type_id'].nunique()
#     multi_target_damage = count_targets[count_targets > 1].values


#     if len(multi_target_damage) == 0:
#         type_most_eficaz = types_ataque.iloc[0]['damage_type_id']
#     else:
#         type_most_eficaz = multi_target_damage[0]



#     oponente_stats = pokemon_stats[pokemon_stats['pokemon_id'] == index]


#     # id,damage_class_id,identifier,is_battle_only,game_index
#     # 1,,hp,0,1
#     # 2,2,attack,0,2
#     # 3,2,defense,0,3
#     # 4,3,special-attack,0,5
#     # 5,3,special-defense,0,6
#     # 6,,speed,0,4
#     # 7,,accuracy,1,
#     # 8,,evasion,1,

#     defense_op = pd.concat([
#         oponente_stats[oponente_stats['stat_id'] == 3],
#         oponente_stats[oponente_stats['stat_id'] == 5]
#     ]).sort_values(by='base_stat', ascending=False)

#     worst_denfese_op = defense_op.iloc[0]['stat_id']
#     best_attack = 2 if worst_denfese_op == 3 else 4


#     # id,identifier
#     # 1,status
#     # 2,physical
#     # 3,special


#     moves = moves[moves['damage_class_id'] != 1]

#     moves = moves[moves['type_id'] == type_most_eficaz]
#     if worst_denfese_op == 3:
#         moves = moves[moves['damage_class_id'] == 2]
#     if worst_denfese_op == 5:
#         moves = moves[moves['damage_class_id'] == 3]

#     moves = moves.sort_values(by=['power', 'accuracy'], ascending=False)


#     golpe_most_power = moves.iloc[0]


#     pokemon_possibles = pokemon_moves[pokemon_moves['move_id'] == golpe_most_power['id']]



#     index_move = 1
#     while len(pokemon_possibles) == 0:  
#         golpe_most_power = moves.iloc[index_move]
#         index_move += 1 
#         pokemon_possibles = pokemon_moves[pokemon_moves['move_id'] == golpe_most_power['id']]





#     pokemon_possibles = pokemon_possibles[pokemon_possibles['version_group_id'] == 25]



#     pokemon_possibles_stats = pokemon_stats[pokemon_stats['stat_id'] == best_attack]


#     pokemon_possibles_stats = pokemon_possibles_stats[pokemon_possibles_stats['pokemon_id'].isin(
#         pokemon_possibles['pokemon_id'])]

#     pokemon_possibles_stats = pokemon_possibles_stats.sort_values(by='base_stat', ascending=False)


#     best_pokemon = pokemon_possibles_stats.iloc[0]


#     dados_escolhidos.append({
#         'Pokemon_Name': best_pokemon['pokemon_id'],  # Supondo que 'identifier' seja o nome do Pokémon
#         'Move_Name': golpe_most_power['identifier'],  # Supondo que 'identifier' seja o nome do movimento
#         'Attack_type': golpe_most_power['damage_class_id'],
#         'Move_type': golpe_most_power['type_id'] 
#     })





dados_df = pd.read_csv('pokemon_moves_chosen.csv')



# Remova valores duplicados do DataFrame
dados_df = dados_df.drop_duplicates()
# Salve o DataFrame como um arquivo CSV
dados_df.to_csv('pokemon_moves_chosen.csv', index=False)


