import json
import os
import re
from typing import Tuple, Union

import elo_mappings

chatpath = "~/.local/share/chatterino/Logs/Twitch/Channels/vedal987/"
LOOKAROUND_LEN = 15
DEBUG = True

chatpath = os.path.expanduser(chatpath)

if DEBUG:
    rejectslist = []

re_messages_comp = []
for expression in elo_mappings.elo_re["message"]:
    re_messages_comp.append(re.compile(expression))
re_anygiftersinchat_comp = []
for expression in elo_mappings.elo_re["anygiftersinthechat"]:
    re_anygiftersinchat_comp.append(re.compile(expression))
re_subs_comp = []
for expression in elo_mappings.elo_re["subs"]:
    re_subs_comp.append(re.compile(expression))
re_sysmessages_comp = []
for expression in elo_mappings.elo_re["sysmessages"]:
    re_sysmessages_comp.append(re.compile(expression))
re_timeouts_comp = []
for expression in elo_mappings.elo_re["timeouts"]:
    re_timeouts_comp.append(re.compile(expression))
re_channelredeems_comp = []
for expression in elo_mappings.elo_re["channelredeems"]:
    re_channelredeems_comp.append(re.compile(expression))

def repass_getuser(message: str, pattern: str) -> str:
    res_re = re.match(pattern, message)
    return res_re.group(1)


def grade_text(message: str, context_ptr: int) -> int:
    return int(elo_mappings.elo_map["normal_message_token"] * len(message) / 10) + 1
    pass

def grade_elo(message: str, context_ptr: int) -> Union[None, Tuple[str, int]]:
    elo_delta = 0
    user_affected = ""

    ### std message
    for expression in re_messages_comp:
        res_re = re.match(expression, message)
        if res_re:
            user_affected = res_re.group(1)
            elo_delta += grade_text(res_re.group(2), context_ptr)
            break

    ### anysubgiftersinchat
    for expression in re_anygiftersinchat_comp:
        res_re = re.match(expression, message)
        if res_re:
            user_affected = res_re.group(1)
            elo_delta += elo_mappings.elo_map["subgift"]
            break

    ### subs
    for expression in re_subs_comp:
        res_re = re.match(expression, message)
        if res_re:
            user_affected = res_re.group(1)
            elo_delta += elo_mappings.elo_map["subs"]
            break

    ### sysmessages
    for expression in re_sysmessages_comp:
        res_re = re.match(expression, message)
        if res_re:
            return None

    ### channelredeems
    for expression in re_channelredeems_comp:
        res_re = re.match(expression, message)
        if res_re:
            user_affected = res_re.group(1)
            elo_delta += elo_mappings.elo_map["channelpointredeems"]
            break

    ### timeouts
    for expression in re_timeouts_comp:
        res_re = re.match(expression, message)
        if res_re:
            user_affected = res_re.group(1)
            elo_delta += elo_mappings.elo_map["timeouts"]
            break

    if elo_delta == 0:
        #print(f"Nodelta: {message}")
        if DEBUG:
            rejectslist.append(message + "\n")
        return None
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

