elo_map = {

    "subs": 10,
    "subgift": 20,
    "normal_message_token": 2,
    "timeouts": -10

}

elo_re = {
    "message" : [r"^\[\d{2}:\d{2}:\d{2}\]  \w*: (.*)$", r"^\[\d{2}:\d{2}:\d{2}\] (\S* \S*):.*$"],
    "anygiftersinthechat": [r"^\[\d{2}:\d{2}:\d{2}\] (\S*) gifted a Tier [123] sub to \S*$"],
    "subs": [r"^\[\d{2}:\d{2}:\d{2}\] (\S*) subscribed (?:with Prime|at Tier [123]). They've subscribed for \d* months(?:!|, currently on a \d* month streak!)$", r"^\[\d{2}:\d{2}:\d{2}\] (\S*) subscribed with Prime.$"],
    "sysmessages": [r"^# Start logging at \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \S*$", r"^\[\d{2}:\d{2}:\d{2}] connected$", r"^\[\d{2}:\d{2}:\d{2}\] disconnected$", r"\[\d{2}:\d{2}:\d{2}\] (\S*) is live!$", r"\[\d{2}:\d{2}:\d{2}\] \S* gifted a Tier [123] sub to \S*! They have given \d* Gift Subs in the channel!$"],
    "timeouts": [r"^\[\d{2}:\d{2}:\d{2}\] (\S*) has been timed out for \S*\. $"]
}


