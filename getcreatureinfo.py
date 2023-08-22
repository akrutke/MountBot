import json
import requests
from blizzardapi import BlizzardApi
import config


extracted_data =[]
def get_creature_info():
    try:
        creatures_family_index = config.api_client.wow.game_data.get_creature_families_index("us", "en_US")
    
        for creature_family in creatures_family_index['creature_families']:
            creature_id = creature_family['id']
            creature_name = creature_family['name']
            extracted_data.append((creature_id,creature_name))     
        for id,name in extracted_data: #save for debugging
            print(f"{id}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
    
    return(extracted_data)
  