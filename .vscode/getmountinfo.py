import json
import requests
from blizzardapi import BlizzardApi
import config

extracted_mount_data =[]

def get_mount_info():
    try:
        mount_index = config.api_client.wow.game_data.get_mounts_index("us", "en_US")
        mount_index_formatted = json.dumps(mount_index,indent=2)
        print(mount_index_formatted)
        
        for mounts in mount_index['mounts']:
            mount_id = mounts['id']
            mount_name = mounts['name']
            extracted_mount_data.append((mount_id,mount_name))
        
        for id,name in extracted_mount_data:
           print(f"Mount: {name}")    
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
    
    return(extracted_mount_data)
 #Need to be abel to pass a name, and have the system look up the id, then use the id to search
 
 #Call blizzard api with user input, return the name of the mount and description
def get_mount_with_id():
    mount_to_search = input("Enter a mount search: ")
    try:
        specific_mount = config.api_client.wow.game_data.get_mount("us", "en_US", mount_to_search)
        cleaned_mount = clean_mount_info(specific_mount)
        if not mount_to_search.isdigit():
            print("Enter digits") 
            return
        if specific_mount:
                for key, value in cleaned_mount.items():
                    print(f"{key}: {value}")
        else:
            print("Mount no found")
    except requests.RequestException as e:
            print("Request failed: {e}")

#Parse out the name and description for the mount
def clean_mount_info(mount_info):
    cleaned_info = {
        "Name: " : mount_info.get('name'),
        "Description: " : mount_info.get('description')
    }
    return cleaned_info