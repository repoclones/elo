import json
import os
import re
from typing import Tuple, Union

from elo_mappings import elo_mappings

chatpath = "~/.local/share/chatterino/Logs/Twitch/Channels/vedal987/"
LOOKAROUND_LEN = 15
DEBUG = True

chatpath = os.path.expanduser(chatpath)

if DEBUG:
    rejectslist = []

def repass_getuser(message: str, pattern: str) -> str:
    res_re = re.match(pattern, message)
    return res_re.group(1)


def grade_text(message: str, context_ptr: int) -> int:
    return int(elo_mappings.elo_map["normal_message_token"] * len(message) / 10) + 1
    pass

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
                    elo_delta += category["elo_award"]
                    user_affected = re_res.group(1)
                    return user_affected, elo_delta
                else:
                    return None


    if not re_matched:
        #print(f"Nodelta: {message}")
        if DEBUG:
            rejectslist.append(message + "\n")
        return None
    raise ValueError(f"matched, but not returned value: {message}")
    return user_affected, elo_delta

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
        grade_elo(message, index)

    if DEBUG:
        with open("./debug_rejects.txt", "w") as f:
            f.writelines(rejectslist)

if __name__ == "__main__":
    main()

