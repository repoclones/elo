import json
import os
import re
from typing import Tuple, Union, List

from elo_mappings import elo_mappings
import grading_functions
import emote_fetcher

chatpath = "~/.local/share/chatterino/Logs/Twitch/Channels/vedal987/"
DEBUG = False

if DEBUG:
    chatpath = "./debug_input_data/"

chatpath = os.path.expanduser(chatpath)

emotelist = emote_fetcher.fetch_all_emotes()
emotedict = {string: True for string in emotelist} # searching from a dict is faster

if DEBUG:
    rejectslist = []
    debuglist = []

def filter_out_strings(original_string: str, strings_to_filter: dict) -> str:
    return ''.join([word + " " for word in original_string.split() if word not in strings_to_filter])

def grade_text(message: str) -> int:
    elo_delta = 0.0

    message = filter_out_strings(message, emotedict)

    if len(message) == 0: # if the message is too small or consists of only 
        return 1

    # add elo based on the message length
    elo_delta += len(message.split()) * 8

    # add elo based on the message's entropy
    elo_delta *= grading_functions.normalization_function_entropy(grading_functions.grade_entropy(message))

    elo_delta *= elo_mappings[0]["elo_award"]
    elo_delta = int(elo_delta) + 1 # base of 1 for sending a message
    if DEBUG:
        len_factor = len(message.split()) * 8
        rand_factor = grading_functions.normalization_function_entropy(grading_functions.grade_entropy(message))
        debuglist.append([[elo_delta, len_factor, rand_factor, grading_functions.grade_entropy(message)], message])
    return elo_delta

def grade_elo(message: str) -> Union[None, Tuple[str, int]]:
    for category in elo_mappings:
        for expression in category["re"]:
            re_res = re.match(expression, message)
            if re_res:
                if category["elo_award"]:
                    user_affected = re_res.group(1)
                    if category["name"] == "stdmessage token":
                        elo_delta = grade_text(re_res.group(2))
                    else:
                        elo_delta = category["elo_award"]
                    return user_affected, elo_delta
                else:
                    return None


    #in case it doens't match
    print(f"WARNING: Unhandled log: {message}")
    if DEBUG:
        rejectslist.append(message + "\n")
    return None

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
    for message in chatlog:
        grade = grade_elo(message)
        if grade:
            user, elo_delta = grade
            if user in elolist:
                elolist[user] += elo_delta
            else:
                elolist[user] = elo_delta

    elolist = dict(sorted(elolist.items(), key=lambda item: item[1], reverse=True))

    ### Write out the new values
    json.dump(elolist, open("debug_elolist.json", "w"), indent=4)

    if DEBUG:
        with open("./debug_rejects.txt", "w") as f:
            f.writelines(rejectslist)

        global debuglist
        debuglist = sorted(debuglist, key=lambda x: x[0][0], reverse=True)
        with open("debug_elodeltas.txt", "w") as f:
            for delta in debuglist:
                f.write(f"{delta[0][0]:< 5}{delta[0][1]:<7}{delta[0][2]:<20}{delta[0][3]:<20}{delta[1]}\n")

if __name__ == "__main__":
    main()

