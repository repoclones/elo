import json
import os
import re
from typing import Tuple, Union, List

from elo_mappings import elo_mappings

chatpath = "~/.local/share/chatterino/Logs/Twitch/Channels/vedal987/"
LOOKAROUND_LEN = 15
DEBUG = True

chatpath = os.path.expanduser(chatpath)

with open("./assets/emotelist.txt") as f:
    emotelist = f.readlines()

emotelist = [s.strip() for s in emotelist]

if DEBUG:
    rejectslist = []

def filter_out_strings(original_string: str, strings_to_filter: List[str]) -> str:
    return ''.join([word for word in original_string.split() if word not in strings_to_filter])

def grade_text(message: str, context_ptr: int) -> int:
    message = filter_out_strings(message, emotelist)
    return int(elo_mappings[0]["elo_award"] * len(message) / 10) + 1

def grade_elo(message: str, context_ptr: int) -> Union[None, Tuple[str, int]]:
    elo_delta = 0
    user_affected = ""
    re_matched = False

    for category in elo_mappings:
        for expression in category["re"]:
            re_res = re.match(expression, message)
            if re_res:
                re_matched = True
                if category["elo_award"]:
                    user_affected = re_res.group(1)
                    if category["name"] == "stdmessage token":
                        elo_delta += grade_text(re_res.group(2), context_ptr)
                    else:
                        elo_delta += category["elo_award"]
                    return user_affected, elo_delta
                else:
                    return None


    if not re_matched:
        print(f"WARNING: Unhandled log: {message}")
        if DEBUG:
            rejectslist.append(message + "\n")
        return None
    raise ValueError(f"matched, but not returned value: {message}")

def main():
    ### Load the chat logs into memory
    chatlist = os.listdir(chatpath)
    chatlog = []
    elolist = {}
    for file in chatlist:
        with open(os.path.join(chatpath, file)) as f:
            this = f.readlines()
        for line in this:
            chatlog.append(line.strip())

    ## time to assign elos
    for index, message in enumerate(chatlog):
        grade = grade_elo(message, index)
        if grade:
            user, elo_delta = grade
            if user in elolist.keys():
                elolist[user] += elo_delta
            else:
                elolist[user] = elo_delta

    json.dump(elolist, open("debug_elolist.json", "w"), indent=4)

    if DEBUG:
        with open("./debug_rejects.txt", "w") as f:
            f.writelines(rejectslist)

if __name__ == "__main__":
    main()

