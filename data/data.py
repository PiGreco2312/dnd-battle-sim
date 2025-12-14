import requests
import os
import re

def clear_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

#---------------------------------------------
def weapon_template():
    weaon_list_dict = [{
        "Name": "Name",
        "Category": "Category",
        "Range": "Range",
        "Damage": "Damage",
        "Type": "Type",
        "Properties": ["Properties"],
        "Mastery": "Mastery"        
    }]

    return weaon_list_dict

def load_weapons():
    # URL per ottenere la lista di tutte le armi
    url = "https://www.dnd5eapi.co/api/2014/equipment-categories/weapon"
    response = requests.get(url)
    
    # Dizionario delle Mastery (Regole 2024)
    #probelmi con nomi armi, alcuni hanno il trattino altri lo spazio
    mastery = {
        "Slow": ["Club", "Crossbow-light", "Javelin", "Sling", "Whip", "Longbow", "Musket"],
        "Nick": ["Dagger", "Light-hammer", "Sickle", "Scimitar"],
        "Push": ["Greatclub", "Pike", "War_Pick", "Crossbow-heavy"],
        "Vex": ["Handaxe", "Dart", "Shortbow", "Rapier", "Shortsword", "Blowgun", "Crossbow-hand", "Pistol"],
        "Sap": ["Mace", "Spear", "Flail", "Morningstar", "Longsword", "Warhammer"],
        "Topple": ["Quarterstaff", "Battleaxe", "Lance", "Maul", "Trident"],
        "Graze": ["Glaive", "Greatsword"],
        "Cleave": ["Halberd", "Greataxe"]
    }
    
    weapon_list = []
    
    if response.status_code == 200:
        data = response.json()
        
        print(f"Trovate {len(data['equipment'])} armi. Scaricamento dettagli in corso...")

        for weapon_ref in data['equipment'][:36]:
            full_url = f"https://www.dnd5eapi.co{weapon_ref['url']}"
            weapon_response = requests.get(full_url)

            if weapon_response.status_code == 200 :
                weapon = weapon_response.json()
                
                new_weapon = {
                    "Name": weapon['index'].capitalize(), 
                    "Category": weapon['weapon_category'].capitalize() if 'weapon_category' in weapon else "No_Category",
                    "Range": weapon['weapon_range'].capitalize() if 'weapon_range' in weapon else "No_Range",
                    "Damage": weapon['damage']['damage_dice'] if 'two_handed_damage' not in weapon else weapon['damage']['damage_dice'] + "/" + weapon['two_handed_damage']['damage_dice'],
                    "Type": weapon['damage']['damage_type']['name'] if 'damage' in weapon else "No_DamageType",
                    "Properties": [prop['name'] for prop in weapon.get('properties', [])],
                    "Mastery": next((key for key, val in mastery.items() if weapon['index'].capitalize() in val), "No_Mastery")
                }
                
                weapon_list.append(new_weapon)

        return weapon_list

    else:
        print(f"Error: {response.status_code}")
        return []

def write_weapons(weapons, filename):
    with open(filename, 'w') as file:
        for weapon in weapons:
            file.write(f"{weapon['Name']},")
            file.write(f"{weapon['Category']},")
            file.write(f"{weapon['Range']},")
            file.write(f"{weapon['Damage']},")
            file.write(f"{weapon['Type']},")
            for prop in weapon['Properties']:
                if prop != weapon['Properties'][-1]:
                    file.write(f"{prop}/")
                else:
                    file.write(f"{prop},")
            file.write(f"{weapon['Mastery']}\n")

#---------------------------------------------------------------------------------------------------------------------------------------
def parse_numeric_speed(speed_str):
    if isinstance(speed_str, str):
        match = re.search(r'\d+', speed_str)
        if match:
            return int(match.group(0))
    return 0

def process_monster_speeds(monster_data):
    source_speeds = monster_data.get('speed', {})

    walk = parse_numeric_speed(source_speeds.get('walk'))
    climb = parse_numeric_speed(source_speeds.get('climb'))
    fly = parse_numeric_speed(source_speeds.get('fly'))
    swim = parse_numeric_speed(source_speeds.get('swim'))

    hover = False # Imposta il valore di default a False.
    if fly > 0:
        hover_value_from_data = source_speeds.get('hover', False)
        hover = bool(hover_value_from_data) 

    final_speeds = {
        "Walk": walk,
        "Climb": climb,
        "Fly": fly,
        "Hover": hover,
        "Swim": swim
    }
    return final_speeds

def monster_template():
    monster_list_dict = [{
        "Name": "Name",
        "Size": "Size",
        "Type": "Type",
        "Alignment": "Alignment",
        "AC": "AC",
        "HP": "HP",
        "Challenge Rating": "CR",
        "Speed": {"Walk": "Walk", "Climb": "Climb", "Fly": "Fly", "Hover": "Hover", "Swim": "Swim"},
        "Vulnerabilities": ["Vulnerabilities"],
        "Resistances": ["Resistances"],
        "Immunities": ["Immunities"],
        
        "Stat": {"STR": 0,   "DEX": 0,   "CON": 0,   "INT": 0,   "WIS": 0,   "CHA": 0},

        "Abilities": [{
            "Name": "Ability_Name",
            "Desc": "Ability_Description"
        }],

        "Actions": [{
            "Name": "Action_Name",
            "Desc": "Action_Description"
        }],
        "Bonus_Actions": [{
            "Name": "Bonus_Action_Name",
            "Desc": "Bonus_Action_Description"
        }],
        "Reactions": [{
            "Name": "Reaction_Name",
            "Desc": "Reaction_Description"
        }],
        "Legendary_Actions": [{
            "Name": "Legendary_Action_Name",
            "Desc": "Legendary_Action_Description"
        }]
    }]

    return monster_list_dict

def load_monsters():
    response = requests.get("https://www.dnd5eapi.co/api/monsters")

    # Initialize the monster list with a template
    monster_list = monster_template()

    # Fetch the list of monsters
    if response.status_code == 200:
        data = response.json()

        #print(f"Trovate {len(data['equipment'])} armi. Scaricamento dettagli in corso...")
        print(f"Trovati {len(data['results'])} mostri. Scaricamento dettagli in corso...")

        for monster in data['results']:
            monster_response = requests.get(f"https://www.dnd5eapi.co{monster['url']}")

            if monster_response.status_code == 200:
                monster = monster_response.json()
                speed = process_monster_speeds(monster)
                monster_list.append({
                    "Name": monster['index'].capitalize(),
                    "Size": monster['size'].capitalize(),
                    "Type": monster['type'].capitalize(),
                    "Alignment": monster['alignment'].capitalize() if 'alignment' in monster else "No_Alignment",
                    "AC": monster['armor_class'][0]['value'] if 'armor_class' in monster else 0,
                    "HP": monster['hit_points'] if 'hit_points' in monster else 0,
                    "Challenge Rating": monster['challenge_rating'] if 'challenge_rating' in monster else 0,

                    "Speed": {
                        type.capitalize(): val
                        for type, val in speed.items()
                    },
                    
                    "Vulnerabilities": [v.capitalize() for v in monster['damage_vulnerabilities']] if 'damage_vulnerabilities' in monster else "No_Vulnerabilities",
                    "Resistances": [r.capitalize() for r in monster['damage_resistances']] if 'damage_resistances' in monster else "No_Resistances",
                    "Immunities": [i.capitalize() for i in monster['damage_immunities']] if 'damage_immunities' in monster else "No_Immunities",                 

                    "Stat": {
                        "STR": monster['strength'] if 'strength' in monster else 0,
                        "DEX": monster['dexterity'] if 'dexterity' in monster else 0,
                        "CON": monster['constitution'] if 'constitution' in monster else 0,
                        "INT": monster['intelligence'] if 'intelligence' in monster else 0,
                        "WIS": monster['wisdom'] if 'wisdom' in monster else 0,
                        "CHA": monster['charisma'] if 'charisma' in monster else 0
                    },

                    "Abilities": [{
                        "Name": ability['name'].capitalize(),
                        "Desc": ability['desc']
                    } for ability in monster['special_abilities']] if 'special_abilities' in monster else "No_Abilities",

                    "Actions": [{
                        "Name": action['name'].capitalize(),
                        "Desc": action['desc']
                    } for action in monster['actions']] if 'actions' in monster else "No_Actions",

                    "Bonus_Actions": [{
                        "Name": action['name'].capitalize(),
                        "Desc": action['desc']
                    } for action in monster['bonus_actions']] if 'bonus_actions' in monster else "No_BonusActions",
                    
                    "Reactions": [{
                        "Name": action['name'].capitalize(),
                        "Desc": action['desc']
                    } for action in monster['reactions']] if 'reactions' in monster else "No_Reactions",

                    "Legendary_Actions": [{
                        "Name": action['name'].capitalize(),
                        "Desc": action['desc']
                    } for action in monster['legendary_actions']] if 'legendary_actions' in monster else "No_LegendaryActions"
                })
        return monster_list
    else:
        print("Errore nel recupero dei mostri.")
        return []

def write_monsters(monsters, filename):
    with open(filename, 'w') as file:
        for monster in monsters:
            file.write(f"{monster['Name']},")
            file.write(f"{monster['Size']},")
            file.write(f"{monster['Type']},")
            file.write(f"{monster['Alignment']},")
            file.write(f"{monster['AC']},")
            file.write(f"{monster['HP']},")
            file.write(f"{monster['Challenge Rating']},")

            speed = monster['Speed']
            for mode, value in speed.items():
                if mode != 'Swim':
                    file.write(f"{value}/")
                else:
                    file.write(f"{value},")

            damage_vector = ['Vulnerabilities', 'Resistances', 'Immunities']
            for attr in damage_vector:
                if monster[attr] is not ("No_Vulnerabilities" or "No_Resistances" or "No_Immunities"):
                    lenght=len(monster[attr])
                    for i, v in enumerate(monster[attr]):
                        if i==lenght-1:
                            file.write(f"{v}/")
                        else:
                            file.write(f"{v},")
                else:
                    file.write(f"{monster[attr]}")
                file.write(",")
            
            stats = monster['Stat']
            for stat, value in stats.items():
                if stat != 'CHA':
                    file.write(f"{value}/")
                else:
                    file.write(f"{value},")

            if monster['Abilities'] != "No_Abilities":
                lenght=len(monster['Abilities'])
                for i, ability in enumerate(monster['Abilities']):
                    if i!=lenght-1:
                        file.write(f"{ability['Name']}:")
                        file.write(f"{ability['Desc']}/")
                    else:
                        file.write(f"{ability['Name']}:")
                        file.write(f"{ability['Desc']},")
            else:
                file.write(f"{monster['Abilities']},")
            
            actions_vector = ['Actions', 'Bonus_Actions', 'Reactions', 'Legendary_Actions']
            for attr in actions_vector:
                if monster[attr] is not ("No_BonusActions" or monster[attr] == "No_Reactions" or monster[attr] == "No_LegendaryActions"):
                    lenght=len(monster[attr])
                    for i, action in enumerate(monster[attr]):
                        if i!=lenght-1:
                            file.write(f"{action['Name']}:")
                            file.write(f"{action['Desc']}/")
                        else:
                            file.write(f"{action['Name']}:")
                            file.write(f"{action['Desc']},")
                else:
                    file.write(f"{monster[attr]},")
            file.write("\n")

#---------------------------------------------------------------------------------------------------------------------------------------
def spell_template():
    spell_list_dict = [{
        "name": "Name",
        "level": "Level", 
        "school": "School",
        "ritual": "Ritual",
        "casting_time": "Casting Time",
        "range": "Range",
        "components": ["Components"],
        "concentration": "Concentration",
        "duration": "Duration",
        "description": ["Description"],
        "attack_type": "Attack Type",
        "area_of_effect":{
            "Type": "Type",
            "Size": "Size"
        },
        #"target": "Target",
        "damage":{
            "Type": "Type",
            "Scaling":[{
                "Level": "Level",
                "Amount": "Amount_damage"
                }]
        },
        "heal":[{
            "Level": "Level",
            "Amount": "Amout_heal"
        }],
        "saving_throw": "Characteristic"
    }]

    return spell_list_dict

def load_spell():
    response = requests.get("https://www.dnd5eapi.co/api/spells")
    spell_list = spell_template()

    if response.status_code == 200:
        data = response.json()
        print(f"Trovati {len(data['results'])-2} incantesimi. Scaricamento dettagli in corso...")

        for spell in data['results']:
            spell_response = requests.get(f"https://www.dnd5eapi.co{spell['url']}")

            if spell_response.status_code == 200:
                spell = spell_response.json()

                #controllo per cantrips
                if spell['level'] == 0:
                    variable = 'damage_at_character_level'
                else:
                    variable = 'damage_at_slot_level'
                
                for d in spell['desc']:
                    d.replace(',', ';') #sostituisco le virgole per evitare problemi nel csv

                spell_list.append({
                    "name": spell['index'].capitalize(),
                    "level": spell['level'],
                    "school": spell['school']['name'],
                    "ritual": spell['ritual'],
                    "casting_time": spell['casting_time'],
                    "range": spell['range'].capitalize(),
                    "components": [c for c in spell['components']] if 'components' in spell else "No_Components",
                    "concentration": spell['concentration'],
                    "duration": spell['duration'].capitalize(),
                    "description": [d for d in spell['desc']],
                    #da cambiare magari, alcune spell di buff debuff non hanno attack type
                    "attack_type": spell['attack_type'].capitalize() if 'attack_type' in spell else "No_AttackType",
                    "area_of_effect":{
                        "Type": spell ['area_of_effect']['type'].capitalize(),
                        "Size": spell ['area_of_effect']['size']                   
                    }if 'area_of_effect' in spell else "No_AreaEffetc",
                    "damage":{
                        #problema con prismatic spray, ha un damage type variabile
                        #problema con sleep, non ha un damage type
                        "Type": spell['damage']['damage_type']['name'] if 'damage' in spell and spell['index']!= 'prismatic-spray' and spell['index']!= 'sleep' else 0,
                        "Scaling":[{
                            "Level": int(n),
                            "Amount": d
                        }for n, d in spell['damage'][variable].items()]
                    }if 'damage' in spell else "No_Damage",
                    "heal": [{
                        "Level": int(n),
                        "Amount": h
                    } for n, h in spell['heal_at_slot_level'].items()] if 'heal_at_slot_level' in spell else "No_Heal",
                    "saving_throw": spell['dc']['dc_type']['name'] if 'dc' in spell else "No_SavingThrow"
                })

        return spell_list
    else:
        print("Errore nel recupero degli incantesimi.")
        return []

def write_spells(spells, filename):
    with open(filename, 'w') as file:

        for spell in spells:
            file.write(f"{spell['name']},")
            file.write(f"{spell['level']},")
            file.write(f"{spell['school']},")
            file.write(f"{'Ritual' if spell['ritual'] else 'No_Ritual'},")
            file.write(f"{spell['casting_time']},")
            file.write(f"{spell['range']},")
            for c in spell['components']:
                if c != spell['components'][-1]:
                    file.write(f"{c}/")
                else:
                    file.write(f"{c},")
            
            file.write(f"{'concentration' if spell['concentration'] else 'No_Concentration'},")
            file.write(f"{spell['duration']},")  
            for d in spell['description']: 
                file.write(f"{d}")
            file.write(",")
            file.write(f"{spell['attack_type']},")
            if spell['area_of_effect'] != "No_AreaEffetc":
                file.write(f"{spell['area_of_effect']['Type']}:{spell['area_of_effect']['Size']},")
            else:
                file.write("No_AreaEffect,")
            
            if spell['damage'] != "No_Damage":
                file.write(f"{spell['damage']['Type']},")
                for scale in spell['damage']['Scaling']:
                    if scale != spell['damage']['Scaling'][-1]:
                        file.write(f"{scale['Level']}:{scale['Amount']}/")
                    else:
                        file.write(f"{scale['Level']}:{scale['Amount']},")
            else:
                file.write("No_Damage,")

            if spell['heal'] != "No_Heal":
                for scale in spell['heal']:
                    if scale != spell['heal'][-1]:
                        file.write(f"{scale['Level']}:{scale['Amount']}/")
                    else:
                        file.write(f"{scale['Level']}:{scale['Amount']},")
            else:
                file.write("No_Heal,")
            file.write(f"{spell['saving_throw']}\n")

#---------------------------------------------------------------------------------------------------------------------------------------

def main():
    clear_terminal()

    # #---------------
    # weapon_list = load_weapons()
    # filename = "weapons.csv"
    # write_weapons(weapon_list, filename)
    # print(f"Weapons data written to {filename}\n")

    #---------------
    spell_list = load_spell()
    filename = "spells.csv"
    write_spells(spell_list, filename)
    print(f"Spells data written to {filename}\n")

    # #---------------
    # monster_list = load_monsters()
    # filename = "monsters.csv"
    # write_monsters(monster_list, filename)
    # print(f"Monsters data written to {filename}\n")


main()