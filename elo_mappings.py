elo_map = {

    "subs": 10,
    "subgift": 20,
    "normal_message_token": 2,
    "timeouts": -10, 
    "channelpointredeems": 10

}

# there is a better way to do it procedually, I will persue that
elo_re = {
    "message" : [r"^\[\d{2}:\d{2}:\d{2}\]  (\w*): (.*)$", r"^\[\d{2}:\d{2}:\d{2}\] (\S* \S*): (.*)$"],
    "anygiftersinthechat": [r"^\[\d{2}:\d{2}:\d{2}\] (\S*) gifted a Tier [123] sub to \S*$"],
    "subs": [r"^\[\d{2}:\d{2}:\d{2}\] (\S*) subscribed (?:with Prime|at Tier [123]). They've subscribed for \d* months(?:!|, currently on a \d* month streak!)$", r"^\[\d{2}:\d{2}:\d{2}\] (\S*) subscribed with Prime.$", r"^\[\d{2}:\d{2}:\d{2}\] (\S*) subscribed at Tier [123].$"],
    "sysmessages": [r"^# Start logging at \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \S*$", r"^\[\d{2}:\d{2}:\d{2}] connected$", r"^\[\d{2}:\d{2}:\d{2}\] disconnected$", r"\[\d{2}:\d{2}:\d{2}\] (\S*) is live!$", r"\[\d{2}:\d{2}:\d{2}\] \S* gifted a Tier [123] sub to \S*! They have given \d* Gift Subs in the channel!$", r"^\[\d{2}:\d{2}:\d{2}\] [MTWFS][a-z]*, \d [JFMASOND][a-z]* \d{4}$", r"^\[\d{2}:\d{2}:\d{2}\] Server connection timed out, reconnecting$", r"^\[\d{2}:\d{2}:\d{2}\] (?:Twitch subscriber|BetterTTV channel|7TV channel) emotes reloaded.$", r"^\[\d{2}:\d{2}:\d{2}\] \S* is continuing the Gift Sub they got from \S*!$", r"^\[\d{2}:\d{2}:\d{2}\] (?:\S*) is now offline.$", r"^\[\d{2}:\d{2}:\d{2}\] You were timed out for .*$", r"^\[\d{2}:\d{2}:\d{2}\] An anonymous user gifted a Tier [123] sub to \S*$", r"^\[\d{2}:\d{2}:\d{2}\] \S* added 7TV emote \S*.$", r"^\[\d{2}:\d{2}:\d{2}\] Failed to fetch (?:BetterTTV|FrankerFaceZ|7TV) channel emotes. \(unknown error\)$", r"^\[\d{2}:\d{2}:\d{2}\] This room is now in slow mode. You may send messages every \d* \S*.$", r"^\[\d{2}:\d{2}:\d{2}\] Failed to load channel badges - OAuth token is missing$", r"^\[\d{2}:\d{2}:\d{2}\] \S* is paying forward the Gift they got from \S* to (?:the community|\S*)!$"],
    "timeouts": [r"^\[\d{2}:\d{2}:\d{2}\] (\S*) has been timed out for (?:\S*|\S* \S*)\.$", r"^\[\d{2}:\d{2}:\d{2}\] (\S*) has been permanently banned.$"],
    "channelredeems": [r"^\[\d{2}:\d{2}:\d{2}\] (\S*) redeemed .*$"]
}


