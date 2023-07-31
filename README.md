# chatelo

## Things to do:

- negative elo for chat bans
- extra elo for gifting subs
- remove fossabot
- ignore simple HUH spam
- ignore EDM

## REGEX

"^\[\d{2}:\d{2}:\d{2}\]  \w*: (.*)$\n"gm

"^\[\d{2}:\d{2}:\d{2}\] (\S*) gifted a Tier [123] sub to \S*$\n"gm
"^# Start logging at \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \S*$\n"gm
"^\[\d{2}:\d{2}:\d{2}] connected$\n"gm
"^\[\d{2}:\d{2}:\d{2}\] (\S*) has been timed out for \S*\. $\n"gm
"^\[\d{2}:\d{2}:\d{2}\] (\S*) subscribed (?:with Prime|at Tier [123]). They've subscribed for \d* months(?:!|, currently on a \d* month streak!)$\n"gm
