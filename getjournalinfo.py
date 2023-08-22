import json
from blizzardapi import BlizzardApi
import config

#journal id for each expansion
def get_journal_id():
    journal_index = config.api_client.wow.game_data.get_journal_expansions_index("us", "en_US")
    journal_index_formatted = json.dumps(journal_index,indent=2)
    print(journal_index_formatted)
    
#parameterize to reuse - for now we know DF is 503
def get_journal_encounter_id():
    journal_encounter_id_index = config.api_client.wow.game_data.get_journal_expansion("us", "en_US",503)
    journal_encounter_id_index_formatted = json.dumps(journal_encounter_id_index,indent=2)
    print(journal_encounter_id_index_formatted)
    
    #hard coding 1208 for now - this is aberrus
def get_journal_instance():
    journal_instance_ids = config.api_client.wow.game_data.get_journal_instance("us", "en_US", 1208)
    journal_instance_ids_formatted = json.dumps(journal_instance_ids,indent=2)
    print(journal_instance_ids_formatted)
    
