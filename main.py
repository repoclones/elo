import json
import os
import re
from typing import Tuple, Union

import elo_mappings

chatpath = "~/.local/share/chatterino/Logs/Twitch/Channels/vedal987/"
LOOKAROUND_LEN = 15

chatpath = os.path.expanduser(chatpath)

def grade_text(message: str, context_ptr: int) -> int:
    pass

def grade_elo(message: str, context_ptr: int) -> Union[None, Tuple[str, int]]:
    elo_delta = 0
    user_affected = ""
    ### Chatmessage
    chat_pattern = r"^\[\d{2}:\d{2}:\d{2}\]  \w*: (.*)$"
    exotic_chat_pattern = r"^\[\d{2}:\d{2}:\d{2}\] (\S* \S*):.*$"

    ### Check for gift message
    giftpattern = r"^\[\d{2}:\d{2}:\d{2}\] (\S*) gifted a Tier [123] sub to \S*$"
    res_gift = re.match(giftpattern, message)
    if res_gift:
        #print(message, end="\t")
        print(res_gift.group(1))
        user_affected = res_gift.group(1)
        elo_delta += elo_mappings.elo_map["subgift"]

    selfgiftpattern = r"^\[\d{2}:\d{2}:\d{2}\] (\S*) subscribed (?:with Prime|at Tier [123]). They've subscribed for \d* months(?:!|, currently on a \d* month streak!)$"
    selfgiftpattern2 = r"^\[\d{2}:\d{2}:\d{2}\] (\S*) subscribed with Prime.$"

    ### Check for system message, messages that don't have any effect on elo
    sys_1 = r"^# Start logging at \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \S*$"
    sys_2 = r"^\[\d{2}:\d{2}:\d{2}] connected$"
    sys_3 = r"^\[\d{2}:\d{2}:\d{2}\] disconnected$"
    islive_pattern = r"\[\d{2}:\d{2}:\d{2}\] (\S*) is live!$"
    trash_gift_pattern = r"\[\d{2}:\d{2}:\d{2}\] \S* gifted a Tier [123] sub to \S*! They have given \d* Gift Subs in the channel!$"
    sys_4 = r"\[\d{2}:\d{2}:\d{2}\] This room is now in slow mode. You may send messages every \d* \w*.$"
    ## to
    timeout_pattern = r"^\[\d{2}:\d{2}:\d{2}\] (\S*) has been timed out for \S*\. $"

    if elo_delta == 0:
        print(f"Nodelta: {message}")
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
    print(len(chatlog))

    ## time to assign elos
    for index, message in enumerate(chatlog):
        grade_elo(message, index)

if __name__ == "__main__":
    main()

