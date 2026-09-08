import requests
import random

def weapons():
    response = requests.get("https://www.dnd5eapi.co/api/equipment-categories/weapon")
    weapon_list = [{
        "Name": "",
        "Weapon Type": "",
        "Damage": 0,
        "Damage Type": "",
        "Properties": [],
        "Mastery": ""
    }]
    if response.status_code == 200:
        data = response.json()
        for weapon in data['equipment']:
            weapon_response = requests.get(f"https://www.dnd5eapi.co{weapon['url']}")

            if weapon_response.status_code == 200:
                weapon = weapon_response.json()
                weapon_list.append({
                    "Name": weapon['name'],
                    "Weapon Type": weapon['weapon_category'] if 'weapon_category' in weapon else 0,
                    "Damage": weapon['damage']['damage_dice'] if 'damage' in weapon else 0,
                    "Damage Type": weapon['damage']['damage_type']['name'] if 'damage' in weapon else "",
                    "Properties": [prop['name'] for prop in weapon['properties']] if 'properties' in weapon else [],
                    # "Mastery": ""  # Placeholder for mastery level
                })
        #print_weapons(weapon_list)
        return weapon_list
    else:
        print("Errore nel recupero delle armi.")
        return []

def print_weapons(weapons):
    for weapon in weapons:
        print(f"Name: {weapon['Name']}")
        print(f"- Type: {weapon['Weapon Type']}")
        print(f"- Damage: {weapon['Damage']} ({weapon['Damage Type']})")
        print(f"- Properties: {', '.join(weapon['Properties']) if weapon['Properties'] else 'None'}")
        #print(f"- Mastery: {weapon['Mastery'] if weapon['Mastery'] else 'None'}")
        print()

def spells():
    response = requests.get("https://www.dnd5eapi.co/api/spells")
    spell_list = [{
        "Name": "",
        "Level": 0,
        "Casting Time": "",
        "Range": "",
        "Components": "",
        "Duration": "",
        "Saving Throw": False,
        "Damage": 0,
    }]
    if response.status_code == 200:
        data = response.json()
        for spell in data['results']:
            spell_response = requests.get(f"https://www.dnd5eapi.co{spell['url']}")

            if spell_response.status_code == 200:
                spell = spell_response.json()
                spell_list.append({
                    "Name": spell['name'],
                    "Level": spell['level'] if 'level' in spell else 0,
                    "Casting Time": spell['casting_time'] if 'casting_time' in spell else "",
                    "Range": spell['range'] if 'range' in spell else "",
                    "Components": ', '.join(spell['components']) if 'components' in spell else "",
                    "Duration": spell['duration'] if 'duration' in spell else "",
                    "Saving Throw": True if 'dc' in spell else False,
                    "Damage": spell['damage']['damage_at_slot_level'] if 'damage' in spell else 0,  #errore nei cantrip
                })
        print_spells(spell_list)
        return spell_list
    else:
        print("Errore nel recupero degli incantesimi.")
        return []

def print_spells(spells):
    for spell in spells:
        print(f"Name: {spell['Name']}")
        print(f"- Level: {spell['Level']}")
        print(f"- Casting Time: {spell['Casting Time']}")
        print(f"- Range: {spell['Range']}")
        print(f"- Components: {spell['Components'] if spell['Components'] else 'None'}")
        print(f"- Duration: {spell['Duration']}")
        print(f"- Saving Throw: {'Yes' if spell['Saving Throw'] else 'No'}")
        if isinstance(spell['Damage'], dict):
            damage_info = ', '.join([f"Slot {level}: {damage}" for level, damage in spell['Damage'].items()])
            print(f"- Damage: {damage_info}")
        else:
            print(f"- Damage: {spell['Damage'] if spell['Damage'] else 'None'}")
        print()

def monsters():
    response = requests.get("https://www.dnd5eapi.co/api/monsters")
    monster_list = [{
        "Name": "",
        "Size": "",
        "Type": "",
        "Alignment": "",
        "AC": 0,
        "HP": 0,
        "Speed": 0,
        "Challenge Rating": 0,
        "Actions": []
    }]
    if response.status_code == 200:
        data = response.json()
        for monster in data['results']:
            monster_response = requests.get(f"https://www.dnd5eapi.co{monster['url']}")

            if monster_response.status_code == 200:
                monster = monster_response.json()
                monster_list.append({
                    "Name": monster['name'],
                    "Size": monster['size'] if 'size' in monster else "",
                    "Type": monster['type'] if 'type' in monster else "",
                    "Alignment": monster['alignment'] if 'alignment' in monster else "",
                    "AC": monster['armor_class'] if 'armor_class' in monster else 0,
                    "HP": monster['hit_points'] if 'hit_points' in monster else 0,
                    "Speed": ', '.join([f"{k} {v} ft." for k, v in monster['speed'].items()]) if 'speed' in monster else 0,
                    "Challenge Rating": monster['challenge_rating'] if 'challenge_rating' in monster else 0,
                    "Actions": [action['name'] for action in monster['actions']] if 'actions' in monster else []
                })
        print_monsters(monster_list)
        return monster_list
    else:
        print("Errore nel recupero dei mostri.")
        return []

def print_monsters(monsters):
    for monster in monsters:
        print(f"Name: {monster['Name']}")
        print(f"- Size: {monster['Size']}")
        print(f"- Type: {monster['Type']}")
        print(f"- Alignment: {monster['Alignment']}")
        print(f"- AC: {monster['AC']}")
        print(f"- HP: {monster['HP']}")
        print(f"- Speed: {monster['Speed']}")
        print(f"- Challenge Rating: {monster['Challenge Rating']}")
        print(f"- Actions: {', '.join(monster['Actions']) if monster['Actions'] else 'None'}")
        print()

def crea_caratteristica(score, pb, proficient):    
    mod = (score - 10) // 2

    if proficient:
        saving_throw = mod + pb
    else:
        saving_throw = mod
    
    Characteristic = {
        "Score": score,
        "Modifier": mod,
        "Saving Throw": saving_throw
    }
    return Characteristic

def pg(lvl, pb, name, hp, ac, speed, con, dex, stg, ing, wis, cha, proficiencies):

    if name == "Quylenna":
        spellcast_ability = "Intelligence"
        spells_known = 6
    elif name == "Deymmond":
        spellcast_ability = "Charisma"
        spells_known = 5
    else:
        spellcast_ability = 0
        spells_known = 0

    character = {
        "Level": lvl,
        "Proficiency Bonus": pb,
        "Name": name,
        "HP": hp,
        "AC": ac,
        "Speed": speed,
        "Characteristics":{
            "Constiturion": crea_caratteristica (con, pb, True),
            "Dexterity": crea_caratteristica (dex, pb, True),
            "Strength": crea_caratteristica (stg, pb, True),
            "Intelligence": crea_caratteristica (ing, pb, True),
            "Wisdom": crea_caratteristica (wis, pb, True),
            "Charisma": crea_caratteristica (cha, pb, True)
        },
        "Class": "",
        "Skills": {
            "Acrobatics": 0,
            "Animal Handling": 0,
            "Arcana": 0,
            "Athletics": 0,
            "Deception": 0,
            "History": 0,
            "Insight": 0,
            "Intimidation": 0,
            "Investigation": 0,
            "Medicine": 0,
            "Nature": 0,
            "Perception": 0,
            "Performance": 0,
            "Persuasion": 0,
            "Religion": 0,
            "Sleight of Hand": 0,
            "Stealth": 0,
            "Survival": 0
        },
        "Actions": [{
            "Attack": {
                "Weapon": {
                    "Name": "",
                    "Attack Bonus": 0,
                    "Damage": {
                        "Dice": "",
                        "Modifier": 0,
                        "Type": ""
                    },
                    "Range": "",
                    "Properties": []
                },
                "Spell": {
                    "Name": "",
                    "Level": 0,
                    "Casting Time": "",
                    "Range": "",
                    "Components": "",
                    "Duration": "",
                    "Saving Throw": False,
                    "Damage": 0,
                }
            },           
        },
            "Dash",
            "Disengage",
            "Dodge",
            "Hide"
        ],
        "Bonus Actions": [
            "Use item"
        ],
        "Reactions": [],
        "Spells": {
            "Spellcasting Ability": spellcast_ability,
            "Spell Save DC": 8+pb+(spellcast_ability-10)//2,
            "Spell Attack Bonus": pb+(spellcast_ability-10)//2,
            "Spell Slots": {
                "1st Level": 0,
                "2nd Level": 0,
                "3rd Level": 0,
                "4th Level": 0,
                "5th Level": 0,
                "6th Level": 0,
                "7th Level": 0,
                "8th Level": 0,
                "9th Level": 0
            },
            "Spells Known": [{
                "Number": spells_known,
                "Spells": [{
                    "Name": "",
                    "Level": 0,
                    "Casting Time": "",
                    "Range": "",
                    "Components": "",
                    "Duration": "",
                    "Saving Throw": False,
                    "Damage": 0,
                    }]   
                }
            ]
        }
    }
    return character

def fight():
    print("Inizia il combattimento!")
    iniziativa_turog = random.randint(1, 20) + (18 - 10) // 2
    iniziativa_deymmond = random.randint(1, 20) + (16 - 10) // 2
    iniziativa_thion = random.randint(1, 20) + (12 - 10) // 2
    iniziativa_raien = random.randint(1, 20) + (10 - 10) // 2
    iniziativa_quylenna = random.randint(1, 20) + (14 - 10) // 2

    iniziative = {
        "Turog": iniziativa_turog,
        "Deymmond": iniziativa_deymmond,
        "Thion": iniziativa_thion,
        "Raien": iniziativa_raien,
        "Quylenna": iniziativa_quylenna
    }

    ordine_iniziativa = sorted(iniziative.items(), key=lambda x: x[1], reverse=True)

    print("Ordine di Iniziativa:")
    for personaggio, iniziativa in ordine_iniziativa:
        print(f"{personaggio}: {iniziativa}")

def main():
    #weapons()
    #spells()   #errore nei cantrip
    #monsters()

    proficiencies = ["Acrobatics", "Stealth", "Arcana", "Investigation"]
    turog = pg(4, 3, "Turog", 45, 18, 30, 16, 18, 14, 10, 12, 8, proficiencies)

    proficiencies = ["Acrobatics", "Stealth", "Arcana", "Investigation"]
    deymmond = pg(4, 3, "Deymmond", 38, 14, 30, 12, 14, 16, 10, 12, 14, proficiencies)

    proficiencies = ["Acrobatics", "Stealth", "Arcana", "Investigation"]
    thion = pg(4, 3, "Thion", 32, 15, 30, 10, 16, 12, 14, 10, 8, proficiencies)

    proficiencies = ["Acrobatics", "Stealth", "Arcana", "Investigation"]
    raien = pg(4, 3, "Raien", 28, 13, 30, 8, 18, 10, 16, 14, 12, proficiencies)

    proficiencies = ["Acrobatics", "Stealth", "Arcana", "Investigation"]
    quylenna = pg(4, 3, "Quylenna", 30, 3, 12, 30, 10, 14, 12, 18, 16, 14, proficiencies)

    #fight()

main()






























# --- Dati di partenza del personaggio ---
lvl = 3
pb = 2
name = "Eldrin"
hp = 25
ac = 16
speed = 30

# Punteggi delle caratteristiche
punteggi = {
    "Constitution": 14,
    "Dexterity": 18,
    "Strength": 10,
    "Intelligence": 16,
    "Wisdom": 12,
    "Charisma": 8
}
# Lista delle competenze nelle abilità
competenze_abilita = ["Acrobatics", "Stealth", "Arcana", "Investigation"]

# Abilità magica
spellcast_ability_score = punteggi["Intelligence"] # Es. Mago

# --- Funzione per creare le caratteristiche (dalla risposta precedente) ---
def crea_caratteristiche(punteggi, bonus_competenza):
    caratteristiche_finali = {}
    for nome, punteggio in punteggi.items():
        modificatore = (punteggio - 10) // 2
        caratteristiche_finali[nome] = {
            "Score": punteggio,
            "Modifier": modificatore,
            "Saving Throw": modificatore + bonus_competenza
        }
    return caratteristiche_finali

# --- Creazione dinamica del dizionario SKILLS ---

# 1. Calcola prima i modificatori per ogni caratteristica
modificatori = {nome: (punteggio - 10) // 2 for nome, punteggio in punteggi.items()}

# 2. Associa ogni abilità al suo modificatore di riferimento
mappa_abilita = {
    "Acrobatics": modificatori["Dexterity"], "Animal Handling": modificatori["Wisdom"],
    "Arcana": modificatori["Intelligence"], "Athletics": modificatori["Strength"],
    "Deception": modificatori["Charisma"], "History": modificatori["Intelligence"],
    "Insight": modificatori["Wisdom"], "Intimidation": modificatori["Charisma"],
    "Investigation": modificatori["Intelligence"], "Medicine": modificatori["Wisdom"],
    "Nature": modificatori["Intelligence"], "Perception": modificatori["Wisdom"],
    "Performance": modificatori["Charisma"], "Persuasion": modificatori["Charisma"],
    "Religion": modificatori["Intelligence"], "Sleight of Hand": modificatori["Dexterity"],
    "Stealth": modificatori["Dexterity"], "Survival": modificatori["Wisdom"]
}

# 3. Genera il dizionario finale delle abilità, aggiungendo il pb solo se c'è competenza
skills_finali = {}
for skill, modifier in mappa_abilita.items():
    if skill in competenze_abilita:
        skills_finali[skill] = modifier + pb
    else:
        skills_finali[skill] = modifier

# --- Assemblaggio finale del personaggio ---
character = {
    "Level": lvl,
    "Proficiency Bonus": pb,
    "Name": name,
    "HP": hp,
    "AC": ac,
    "Speed": speed,
    "Characteristics": crea_caratteristiche(punteggi, pb), # Chiamata singola e pulita
    "Skills": skills_finali, # Dizionario generato dinamicamente e correttamente
    "Actions": [],
    "Bonus Actions": [],
    "Reactions": [],
    "Spells": {
        "Spellcasting Ability": "Intelligence",
        "Spell Save DC": 8 + pb + modificatori["Intelligence"],
        "Spell Attack Bonus": pb + modificatori["Intelligence"],
        "Spell Slots": { "1st Level": 4, "2nd Level": 2, "3rd Level": 0, "4th Level": 0, "5th Level": 0, "6th Level": 0, "7th Level": 0, "8th Level": 0, "9th Level": 0 },
        "Spells Known": { # SINTASSI CORRETTA
            "Number": 0,
            "Spells": []
        }
    }
}

import pprint
pprint.pprint(character)
