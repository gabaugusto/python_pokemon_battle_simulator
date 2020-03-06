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
      if nature == 1 and target == "attack":
              nature = ben_nature
      if nature == 1 and target == "sp_attack":
              nature = hin_nature
      else:
              nature = neu_nature
      
      return nature

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
      def __init__(self, name, id, level, happiness, form, weight, nature, type_01, type_02, base_hp, base_attack, base_defense, base_sp_attack, base_sp_defense, base_speed, ev_hp, ev_attack, ev_defense, ev_sp_attack, ev_sp_defense, ev_speed, iv_hp, iv_attack, iv_defense, iv_sp_attack, iv_sp_defense, iv_speed, attach_item, ability, status, accuracy, evasion, team):
  
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
              self.move_01 = Moves("Body Slam", 1, 1, 1, 8, 80, 100, "paralyze", 20)
              self.move_02 = Moves("Earthquake", 1, 1, 1, 8, 100, 100, "none", 0)
              self.move_03 = Moves("Fire Punch", 1, 1, 1, 8, 60, 100, "burn", 30)
              self.move_04 = Moves("Crunch", 1, 1, 1, 8, 80, 100, "flinch", 10)
           
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
			
pokemon_01 = Pokemon("Snorlax", id, 100, 255, 255, 0, 1, 1, 0, 160, 110, 65, 65, 110, 30, 252, 0, 252, 0, 4, 0, 31, 0, 0, 31, 31, 0, 0, 55, 0, 100, 100, 1)
pokemon_03 = Pokemon("Arcanine", id, 100, 255, 255, 0, 1, 3, 0, 79, 83, 100, 85, 105, 78, 252, 0, 4, 252, 0, 0, 31, 31, 31, 31, 31, 31, 0, 55, 0, 100, 100, 2)
pokemon_05 = Pokemon("Suicune", id, 100, 255, 255, 0, 1, 3, 0, 79, 83, 100, 85, 105, 78, 252, 0, 4, 252, 0, 0, 31, 31, 31, 31, 31, 31, 0, 55, 0, 100, 100, 2)
pokemon_07 = Pokemon("Mew", id, 100, 255, 255, 0, 1, 3, 0, 100, 100, 100, 100, 100, 100, 252, 0, 4, 252, 0, 0, 31, 31, 31, 31, 31, 31, 0, 55, 0, 100, 100, 2)
pokemon_09 = Pokemon("Gengar", id, 100, 255, 255, 0, 1, 3, 0, 100, 100, 100, 100, 100, 100, 252, 0, 4, 252, 0, 0, 31, 31, 31, 31, 31, 31, 0, 55, 0, 100, 100, 2)
pokemon_11 = Pokemon("Rapidash", id, 100, 255, 255, 0, 1, 3, 0, 100, 100, 100, 100, 100, 100, 252, 0, 4, 252, 0, 0, 31, 31, 31, 31, 31, 31, 0, 55, 0, 100, 100, 2)
team_a = [pokemon_01, pokemon_03, pokemon_05, pokemon_07, pokemon_09, pokemon_11]

#self, name, id, level, happiness, weight, nature, type_01, type_02, base_hp, base_attack, base_defense, base_sp_attack, base_sp_defense, base_speed, ev_hp, ev_attack, ev_defense, ev_sp_attack, ev_sp_defense, ev_speed, iv_hp, iv_attack, iv_defense, iv_sp_attack, iv_sp_defense, iv_speed, type_1, type_2, attach_item, ability, status, accuracy, evasion, team
pokemon_02 = Pokemon("Blastoise", id, 100, 255, 255, 0, 1, 3, 0, 79, 83, 100, 85, 105, 78, 252, 0, 4, 252, 0, 0, 31, 31, 31, 31, 31, 31, 0, 55, 0, 100, 100, 2)
pokemon_04 = Pokemon("Charizard", id, 100, 255, 255, 0, 1, 3, 0, 79, 83, 100, 85, 105, 78, 252, 0, 4, 252, 0, 0, 31, 31, 31, 31, 31, 31, 0, 55, 0, 100, 100, 2)
pokemon_06 = Pokemon("Snorlax", id, 100, 255, 255, 0, 1, 3, 0, 79, 83, 100, 85, 105, 78, 252, 0, 4, 252, 0, 0, 31, 31, 31, 31, 31, 31, 0, 55, 0, 100, 100, 2)
pokemon_08 = Pokemon("Raichu", id, 100, 255, 255, 0, 1, 3, 0, 79, 83, 100, 85, 105, 78, 252, 0, 4, 252, 0, 0, 31, 31, 31, 31, 31, 31, 0, 55, 0, 100, 100, 2)
pokemon_10 = Pokemon("Lapras", id, 100, 255, 255, 0, 1, 3, 0, 79, 83, 100, 85, 105, 78, 252, 0, 4, 252, 0, 0, 31, 31, 31, 31, 31, 31, 0, 55, 0, 100, 100, 2)
pokemon_12 = Pokemon("Venusaur", id, 100, 255, 255, 0, 1, 3, 0, 79, 83, 100, 85, 105, 78, 252, 0, 4, 252, 0, 0, 31, 31, 31, 31, 31, 31, 0, 55, 0, 100, 100, 2)
team_b = [pokemon_02, pokemon_04, pokemon_06, pokemon_08, pokemon_10, pokemon_12]

class Character:
      """
      Base class used to create Character that hold the teams 
      """
      def __init__(self, name, id, team):
        self.name = name
        self.id = id 
        self.team = team  
			  
      def check_team(self, name, id, team):
        if self.team.count > 0:
          pass
				

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
      type_calculation = 1
      
      attacker_name = attacker.name
      attacker_id = attacker.id 
      attacker_level = attacker.level
      attacker_stat = ""
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
      defender_stat = 0
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
      if move_category == 1:
              defender_stat = defender_stat_defense
              attacker_stat = attacker_stat_attack
      elif move_category == 2:
              defender_stat = defender_stat_special_defense
              attacker_stat = attacker_stat_special_attack

      #Calc Assault Vest
      if defender_attach_item == 22 and move_category == 2:
              defender_stat_special_defense = defender_stat_special_defense * 1.25 

      #Calc Muscle Band
      if move_category == 1 and attacker_attach_item == 8:
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
			  
      #Calc Modifiers
      modifier = weather_mod * badge * critical * random_mod * stab * type_calculation * burn_mod

      #Calc Damage
      damage = (((((2 * attacker_level)/5 + 2) * move_power * (attacker_stat/defender_stat))/50) + 2 ) * modifier

      #Calc LifeOrb
      if attacker_attach_item == 15:
              damage = damage * 1.3
              self_damage_calculation(attacker_current_hp, 0.3)

      #Calc Berries
      if defender_attach_item == 10:
              damage = damage * 0.8
        
      damage = round(damage)
      defender_previous_hp = ""
      defender_previous_hp = defender.current_hp
      defender.current_hp = defender.current_hp - damage
      #print("===== Damage Calculation")
      #print("_weather_mod", weather_mod)
      #print("___move_type", move_type)
      #print("____critical", critical)
      #print("______random", random_mod)
      #print("________stab", stab)
      #print("________burn", burn_mod)
      #print("____modifier", modifier)
      #print("______damage", damage)
      print_damage(attacker_name, move_name, damage)
      defender.update_status(defender.current_hp, defender_current_hp)
      
      print(defender.name, "had", defender_previous_hp, "and now it has", defender.current_hp)
      print("Attacker HP", attacker.current_hp)
      print("Defender HP", defender.current_hp)
      return damage

def random_climate(pokemon_01, pokemon_02):
    pass

def turn(pokemon_01, pokemon_02):

    if __name__ == '__main__':
      game_in_progress = True
      while game_in_progress:
          
        print(pokemon_01.name, "is out")
        print(pokemon_02.name, "is out")
        move_list = [pokemon_01.move_01, pokemon_01.move_02, pokemon_01.move_03, pokemon_01.move_04, "Change Pokemon"]

        move_list_opponent =  [pokemon_02.move_01, pokemon_02.move_02, pokemon_02.move_03, pokemon_02.move_04]   

        action = 0

        while not int(action) in range(1,5): 
          print('What will', pokemon_01.name, "do?")
          print("\n[1]", move_list[0].name, "\n[2]", move_list[1].name, "\n[3]", move_list[2].name, "\n[4]", move_list[3].name, "\n\n[5] " + move_list[4])
          action = int(input(" "))

        action = action - 1
        chosen_move = move_list[action]

        randon_choice = random.randint(0, 3)
        chosen_move_opponent = move_list_opponent[randon_choice]

        #checkPriority
        Moves.action("", action, pokemon_01, pokemon_02)
        if game_in_progress == True:
          Moves.action("", randon_choice, pokemon_02, pokemon_01)
                  
        if pokemon_01.current_hp <= 0:
          #team_a.remove[pokemon_01]
          
          for n in team_a:
            print(team_a[n])
          game_in_progress = False
          print('game!')          

        elif pokemon_02.current_hp <= 0:
          #team_b.remove[pokemon_01]
          for n in team_b:
            print(team_b[n])
          game_in_progress = False

          print('game!')

turn(pokemon_01, pokemon_02)