"""
main.py
Pokemon Battle Simulator
"""
import random
import json

#Nature Resolution
def calc_nature(nature, target):

      ben_nature = 1.1
      hin_nature = 0.9
      neu_nature = 1.0

      if nature == 'adamant' and target == "attack":
              nature = ben_nature
      if nature == 'adamant' and target == "sp_attack":
              nature = hin_nature            
      if nature == 'modest' and target == "attack":
              nature = hin_nature
      if nature == 'modest' and target == "sp_attack":
              nature = ben_nature   
      if nature == 'bold' and target == "attack":
              nature = hin_nature
      if nature == 'bold' and target == "defense":
              nature = ben_nature    
      if nature == 'calm' and target == "attack":
              nature = hin_nature
      if nature == 'calm' and target == "defense":
              nature = ben_nature                            
      if nature == 'timid' and target == "attack":
              nature = hin_nature
      if nature == 'timid' and target == "speed":
              nature = ben_nature
      else:
              nature = neu_nature
      return nature

def calc_types(move_type, type_def_01, type_def_02):
  #USAGE calc_types(power, move_type, type_def_01, type_def_02)    
  power = 1
  with open('eff.json') as json_file:
    data = json.load(json_file)

    if data['super_effective'][move_type]:
      if type_def_01 in data['super_effective'][move_type]:
        power *= 2

    if data['super_effective'][move_type]:
      if type_def_02 in data['super_effective'][move_type]:
        power *= 2        

    if data['normal_effective'][move_type]:
      if type_def_01 in data['normal_effective'][move_type]:
        power *= 1       

    if data['normal_effective'][move_type]:
      if type_def_02 in data['normal_effective'][move_type]:
        power *= 1              

    if data['not_very_effective'][move_type]:
      if type_def_01 in data['not_very_effective'][move_type]:
        power *= 0.5       

    if data['not_very_effective'][move_type]:
      if type_def_02 in data['not_very_effective'][move_type]:
        power *= 0.5       

    if data['no_effect'][move_type]:
      if type_def_01 in data['no_effect'][move_type]:
        power *= 0      

    if data['no_effect'][move_type]:
      if type_def_02 in data['no_effect'][move_type]:
        power *= 0  

    if power > 1: 
      print('Super Effective', power)
    if power < 1: 
      print('Not Very Effective', power)

    return power

class Moves:
      """
      Base class used to create Moves
      """
      def __init__(self, name, category, move_type, id, pp, power, acc, sec_eff, percent_eff):
              self.name = name
              self.id = id 
              self.category = category
              self.type = move_type
              self.pp = pp  
              self.power = power
              self.acc = acc 
              self.sec_eff = sec_eff 
              self.percent_eff = percent_eff  

      def action(self, id, pokemon_01, pokemon_02):
              damage_calculation(id, pokemon_01, pokemon_02)
              if pokemon_01.current_hp <= 0 or pokemon_02.current_hp <= 0:
                game_in_progress = False       

class Pokemon:
      """
      Base class used to create Pokemons
      """

      def __init__(self, name, id, level, happiness, form, weight, nature, type_01, type_02, base_hp, base_attack, base_defense, base_sp_attack, base_sp_defense, base_speed, ev_hp, ev_attack, ev_defense, ev_sp_attack, ev_sp_defense, ev_speed, iv_hp, iv_attack, iv_defense, iv_sp_attack, iv_sp_defense, iv_speed, attach_item, ability, status, accuracy, evasion, team, move_01, move_02, move_03, move_04):

        self.name = name
        self.id = id 
        self.level = level
        self.happiness = happiness
        self.form = form
        self.weight = weight
        self.nature = nature
        self.type_01 = type_01
        self.type_02 = type_02
        self.attach_item = attach_item
        self.ability = ability
        self.status = status
        self.base_hp = base_hp
        self.base_attack = base_attack
        self.base_defense = base_defense
        self.base_sp_attack = base_sp_attack
        self.base_sp_defense = base_sp_defense
        self.base_speed = base_speed    
        self.ev_hp = ev_hp
        self.ev_attack = ev_attack
        self.ev_defense = ev_defense
        self.ev_sp_attack = ev_sp_attack
        self.ev_sp_defense = ev_sp_defense
        self.ev_speed = ev_speed
        self.iv_hp = iv_hp
        self.iv_attack = iv_attack
        self.iv_defense = iv_defense
        self.iv_sp_attack = iv_sp_attack
        self.iv_sp_defense = iv_sp_defense
        self.iv_speed = iv_speed
        self.hp = ((((2 * base_hp) + iv_hp + (ev_hp/4)) * level)/100)  + level + 10
        self.current_hp = self.hp 
        self.attack = (((((2 * base_attack) + iv_attack + (ev_attack/4)) * level)/100)  + 5) * calc_nature(nature, "attack")
        self.defense = (((((2 * base_defense) + iv_defense + (ev_defense/4)) * level)/100)  + 5) * calc_nature(nature, "defense")
        self.sp_attack = (((((2 * base_sp_attack) + iv_sp_attack + (ev_sp_attack/4)) * level)/100)  + 5) * calc_nature(nature, "sp_attack")
        self.sp_defense = (((((2 * base_sp_defense) + iv_sp_defense + (ev_sp_defense/4)) * level)/100)  + 5) * calc_nature(nature, "sp_defense")
        self.speed = (((((2 * base_speed) + iv_speed + (ev_speed/4)) * level)/100)  + 5) * calc_nature(nature, "speed")
        self.accuracy = accuracy
        self.evasion = evasion
        self.team = team

        self.move_01 = move_01
        self.move_02 = move_02
        self.move_03 = move_03
        self.move_04 = move_04

      def update_status(self, target, value):
        self.target = value

      def change_form(self, form, value, f_attack, f_defense, f_sp_attack, f_sp_defense, f_speed, f_ability):

        update_status(form, value)
        update_status(self.attack, f_attack)
        update_status(self.defense, f_defense)
        update_status(self.sp_attack, f_sp_attack)
        update_status(self.sp_defense, f_sp_defense)
        update_status(self.speed, f_speed)
        update_status(self.ability, f_ability)

class Character:
      """
      Base class used to create Character that hold the teams, pokemons and moves
      """
      #USAGE
      def __init__(self, id):
        with open('base.json') as json_file:
          base = json.load(json_file)
          id = 'player_0' + str(id)
          self.name = base[id]['Name']
          self.region = base[id]['Region']
          self.ai = base[id]['AI']
          self.message_victory = base[id]['victory']
          self.message_defeat = base[id]['defeat']
         
          #print(base[id]['pokemon_01']['moves'])

          self.pokemon_01 = Pokemon(base[id]['pokemon_01']['name'], base[id]['pokemon_01']['pokedex'], base[id]['pokemon_01']['level'], base[id]['pokemon_01']['happiness'], base[id]['pokemon_01']['happiness'], base[id]['pokemon_01']['weight'], base[id]['pokemon_01']['nature'], base[id]['pokemon_01']['type'][0], base[id]['pokemon_01']['type'][1], base[id]['pokemon_01']['base_stats'][0]['hp'], base[id]['pokemon_01']['base_stats'][0]['attack'], base[id]['pokemon_01']['base_stats'][0]['defense'], base[id]['pokemon_01']['base_stats'][0]['sp_attack'], base[id]['pokemon_01']['base_stats'][0]['sp_defense'], base[id]['pokemon_01']['base_stats'][0]['speed'], base[id]['pokemon_01']['base_evs'][0]['hp'], base[id]['pokemon_01']['base_evs'][0]['attack'], base[id]['pokemon_01']['base_evs'][0]['defense'], base[id]['pokemon_01']['base_evs'][0]['sp_attack'], base[id]['pokemon_01']['base_evs'][0]['sp_defense'], base[id]['pokemon_01']['base_evs'][0]['speed'], base[id]['pokemon_01']['base_ivs'][0]['hp'], base[id]['pokemon_01']['base_ivs'][0]['attack'], base[id]['pokemon_01']['base_ivs'][0]['defense'], base[id]['pokemon_01']['base_ivs'][0]['sp_attack'], base[id]['pokemon_01']['base_ivs'][0]['sp_defense'], base[id]['pokemon_01']['base_ivs'][0]['speed'], base[id]['pokemon_01']['attach_item'], base[id]['pokemon_01']['ability'], base[id]['pokemon_01']['status'], base[id]['pokemon_01']['accuracy'], base[id]['pokemon_01']['evasion'],1, Moves(base[id]['pokemon_01']['moves'][0]['move_01'][0]['name'], base[id]['pokemon_01']['moves'][0]['move_01'][0]['category'], base[id]['pokemon_01']['moves'][0]['move_01'][0]['type'], base[id]['pokemon_01']['moves'][0]['move_01'][0]['id'], base[id]['pokemon_01']['moves'][0]['move_01'][0]['pp'], base[id]['pokemon_01']['moves'][0]['move_01'][0]['power'], base[id]['pokemon_01']['moves'][0]['move_01'][0]['acc'], base[id]['pokemon_01']['moves'][0]['move_01'][0]['sec_eff'], base[id]['pokemon_01']['moves'][0]['move_01'][0]['percent_eff']), Moves(base[id]['pokemon_01']['moves'][0]['move_02'][0]['name'], base[id]['pokemon_01']['moves'][0]['move_02'][0]['category'], base[id]['pokemon_01']['moves'][0]['move_02'][0]['type'], base[id]['pokemon_01']['moves'][0]['move_02'][0]['id'], base[id]['pokemon_01']['moves'][0]['move_02'][0]['pp'], base[id]['pokemon_01']['moves'][0]['move_02'][0]['power'], base[id]['pokemon_01']['moves'][0]['move_02'][0]['acc'], base[id]['pokemon_01']['moves'][0]['move_02'][0]['sec_eff'], base[id]['pokemon_01']['moves'][0]['move_02'][0]['percent_eff']), Moves(base[id]['pokemon_01']['moves'][0]['move_03'][0]['name'], base[id]['pokemon_01']['moves'][0]['move_03'][0]['category'], base[id]['pokemon_01']['moves'][0]['move_03'][0]['type'], base[id]['pokemon_01']['moves'][0]['move_03'][0]['id'], base[id]['pokemon_01']['moves'][0]['move_03'][0]['pp'], base[id]['pokemon_01']['moves'][0]['move_03'][0]['power'], base[id]['pokemon_01']['moves'][0]['move_03'][0]['acc'], base[id]['pokemon_01']['moves'][0]['move_03'][0]['sec_eff'], base[id]['pokemon_01']['moves'][0]['move_03'][0]['percent_eff']), Moves(base[id]['pokemon_01']['moves'][0]['move_04'][0]['name'], base[id]['pokemon_01']['moves'][0]['move_04'][0]['category'], base[id]['pokemon_01']['moves'][0]['move_04'][0]['type'], base[id]['pokemon_01']['moves'][0]['move_04'][0]['id'], base[id]['pokemon_01']['moves'][0]['move_04'][0]['pp'], base[id]['pokemon_01']['moves'][0]['move_04'][0]['power'], base[id]['pokemon_01']['moves'][0]['move_04'][0]['acc'], base[id]['pokemon_01']['moves'][0]['move_04'][0]['sec_eff'], base[id]['pokemon_01']['moves'][0]['move_04'][0]['percent_eff']))

      def check_team(self, name, id, team):
        if self.team.count > 0:
          pass

player = Character(0)    
npc = Character(1)    
print(player.pokemon_01.name)
game_in_progress = True
battle_in_progress = True
turn_in_progress = True

####################### - Print Functions
def print_damage(target, move, damage):
      print('{} used {}. It dealt {} damage.'.format(target, move, damage))

def print_self_damage(target, move, damage):
      print('{} used was hurt in {} damage.'.format(target, damage))  

####################### - Damages
### Self Damage Calculation ###

def self_damage_calculation(target_current_hp, damage):
      target_current_hp -= target_current_hp * 0.3
      #print (target_current_hp)
      return target_current_hp

### Damage Calculation ###
def damage_calculation(move, attacker, defender):

      #Definitions
      modifier = 0
      damage = 0
      move = int(move)
      random_mod = 1.0
      move_choice = [attacker.move_01, attacker.move_02, attacker.move_03, attacker.move_04]
      move_name = move_choice[move].name
      move_type = move_choice[move].type
      move_power = move_choice[move].power
      move_category = move_choice[move].category

      attacker_name = attacker.name
      attacker_id = attacker.id 
      attacker_level = attacker.level
      attacker_stat = 1
      attacker_stat_attack = attacker.attack
      attacker_stat_special_attack = attacker.sp_attack     
      attacker_type_1 = attacker.type_01
      attacker_type_2 = attacker.type_02
      attacker_attach_item = attacker.attach_item
      attacker_ability = attacker.ability
      attacker_status = attacker.status
      attacker_full_hp = attacker.hp
      attacker_current_hp = attacker.hp

      defender_name = defender.name
      defender_id = defender.id
      defender_level = defender.level
      defender_stat = 1
      defender_stat_defense = defender.defense
      defender_stat_special_defense = defender.sp_defense
      defender_type_1 = defender.type_01
      defender_type_2 = defender.type_02
      defender_attach_item = defender.attach_item
      defender_ability = defender.ability
      defender_status = defender.status
      defender_full_hp = defender.hp
      defender_previous_hp = ""
      defender_current_hp = defender.hp
      defender_imunity = False

      weather = 1
      weather_mod = 1
      badge = 1
      burn_mod = 1
      screen_special = False
      screen_physical = False

      if attacker_status == 3 or attacker_status == 3:
        attacker_stat_attack = attacker_stat_attack/2

      #Category Attack      
      if move_category == "Physical":
        defender_stat = defender_stat_defense
        attacker_stat = attacker_stat_attack

      elif move_category == "Special":
        defender_stat = defender_stat_special_defense
        attacker_stat = attacker_stat_special_attack

      #Calc Assault Vest
      if defender_attach_item == 22 and move_category == 2:
        defender_stat_special_defense = defender_stat_special_defense * 1.25

      #Calc Muscle Band
      if move_category == "Physical" and attacker_attach_item == 8:
        move_power = move_power * 1.3

      #Calc Rain and Harsh Sunlight
      if weather == 2 and move_type == 2:
        weather_mod = 1.5

      elif weather == 3 and move_type == 3:
        weather_mod = 1.5

      #Calc critical  
      critical = 1

      #Calc randon
      random_mod = random.uniform(0.85, 1.0)

      #Calc stab
      stab = 1
      if attacker_type_1 == move_type or attacker_type_2 == move_type:
        stab = 1.5

      if attacker_type_1 == move_type and attacker_ability == 2 or attacker_type_2 == move_type and attacker_ability == 2:
        stab = 2  

      type_calculation = calc_types(move_type, defender_type_1, defender_type_2)
      print("type_calculation:", type_calculation)

      #Calc Modifiers
      modifier = int(weather_mod) * int(badge) * int(critical) * float(random_mod) * int(stab) * int(type_calculation) * int(burn_mod)
      modifier += 1

      #Calc Damage
      damage = (((((2 * attacker_level)/5 + 2) * move_power * (attacker_stat/defender_stat))/50) + 2 ) * modifier
      print(damage)
      #Calc LifeOrb
      if attacker_attach_item == 'life_orb':
              damage = damage * 1.3
              self_damage_calculation(attacker_current_hp, 0.3)

      #Calc Berries
      if defender_attach_item == 10:
              damage = damage * 0.8

      damage = round(damage)
      defender_previous_hp = ""
      defender_previous_hp = defender.current_hp
      defender.current_hp = defender.current_hp - damage

      print_damage(attacker_name, move_name, damage)
      defender.update_status(defender.current_hp, defender_current_hp)

      print(defender.name, "had", defender_previous_hp, "and now it has", defender.current_hp)
      percent_hp_defender = (attacker.current_hp * 100/attacker.hp) 
      print("Attacker HP", attacker.current_hp)
      print("Defender HP", defender.current_hp, "(",percent_hp_defender,"%)")
      return damage

def random_climate(pokemon_01, pokemon_02):

    pass



def game(player, npc, game_in_progress):
  game_in_progress = game_in_progress
  while game_in_progress:
    pokemon_01 = player.pokemon_01
    pokemon_02 = npc.pokemon_01
    battle(player, npc, pokemon_01, pokemon_02, game_in_progress) 

def battle(player, npc, pokemon_01, pokemon_02, battle_in_progress):
  battle_in_progress = battle_in_progress
  while battle_in_progress:
    turn(pokemon_01, pokemon_02, turn_in_progress) 

def turn(pokemon_01, pokemon_02, turn_in_progress):
  turn_in_progress = turn_in_progress
  while turn_in_progress:
    print(pokemon_01.name, "is out")
    print(pokemon_02.name, "is out")
    turn_counter = 1

    print('turn: ', turn_counter)
    move_list = [pokemon_01.move_01, pokemon_01.move_02, pokemon_01.move_03, pokemon_01.move_04, "Change Pokemon"]

    move_list_opponent = [pokemon_02.move_01, pokemon_02.move_02, pokemon_02.move_03, pokemon_02.move_04]   
    action = 0

    while not int(action) in range(1,5): 
      print('Turn ', turn_counter)
      print('What will', pokemon_01.name, "do?")
      print("\n[1]", move_list[0].name, "\n[2]", move_list[1].name, "\n[3]", move_list[2].name, "\n[4]", move_list[3].name, "\n\n[5] " + move_list[4])

      action = int(input(" "))

    action = action - 1
    chosen_move = move_list[action]
    randon_choice = random.randint(0, 3)
    chosen_move_opponent = move_list_opponent[randon_choice]

    #checkPriority
    if chosen_move.category != "Other":
      Moves.action("", action, pokemon_01, pokemon_02)
    if turn_in_progress == True:
      if chosen_move_opponent.category != "Other":
        Moves.action("", randon_choice, pokemon_02, pokemon_01)
  

    if pokemon_01.current_hp <= 0:
      print(pokemon_01.name, 'was knocked out.')
      print('game!')          
      turn_in_progress = False

    elif pokemon_02.current_hp <= 0:
      print(pokemon_02.name, 'was knocked out.')
      print('game!')
      turn_in_progress = False


game(player, npc, game_in_progress)  
