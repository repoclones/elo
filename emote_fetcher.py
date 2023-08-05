import requests
import os
from typing import List
import time
import json

cache_dir = "assets/.cache"
MAX_CACHE_AGE = 23 * 3600 # 23 hours

if not os.path.exists(cache_dir):
    os.mkdir(cache_dir)


seventv_origin = "7tv.io"
seventv_interested_emote_set = "63a74bb4b9e2887125268ebb"

def fetch_seventv_emotes() -> List[str]:
    """
    This function is responisble for fetching 7TV emotes, and managing the cache of the request
    """
    cache_filename = f"seventv-emote-set-{seventv_interested_emote_set}"
    if os.path.exists(os.path.join(cache_dir, cache_filename)):
        emote_dict = json.load(open(os.path.join(cache_dir, cache_filename)))
        if emote_dict["fetch_timestamp"] > int(time.time()) - MAX_CACHE_AGE: # cache is still valid
            return emote_dict["emote_list"]
    r = requests.get(f"https://{seventv_origin}/v3/emote-sets/{seventv_interested_emote_set}")
    response_dict = r.json()
    emote_dict = {"fetch_timestamp": int(time.time()), "emote_list": []}
    for emote in response_dict["emotes"]:
        emote_dict["emote_list"].append(emote["name"])
    json.dump(emote_dict, open(os.path.join(cache_dir, cache_filename), "w"))
    return emote_dict["emote_list"]

def fetch_other_emotes():
    with open("assets/emotelist.txt") as f:
        emotelist = f.readlines()
    emotelist = [s.strip() for s in emotelist]
    return emotelist

def fetch_all_emotes():
    all_emotes = []
    all_emotes += fetch_seventv_emotes()
    all_emotes += fetch_other_emotes()
    return all_emotes

if __name__ == "__main__":
    #fetch_seventv_emotes()
    #fetch_other_emotes()
    all_emotes = fetch_all_emotes()
    print(f"Total of {all_emotes} emotes")
