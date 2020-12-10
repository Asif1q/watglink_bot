"""Emoji
Available Commands:
.dick
`@rooternobody`"""

from telethon import events

import asyncio

from userbot.events import register

@register(outgoing=True, pattern="^.dick")
async def dick(event):
    if event.fwd_from:
        return
    animation_interval = 2.5
    animation_ttl = range(0, 1)
    animation_chars = ['...............▄▄ ▄▄\n......▄▌▒▒▀▒▒▐▄\n.... ▐▒▒▒▒▒▒▒▒▒▌\n... ▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▒▒▒▒▒▒▒▒▒▒▒▌\n....▐▀▄▄▄▄▄▄▄▄▄▀▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n....▐░░░░░░░░░░░▌\n...▄█▓░░░░░░░░░▓█▄\n..▄▀░░░░░░░░░░░░░ ▀▄\n.▐░░░░░░░▀▄▒▄▀░░░░░░▌\n▐░░░░░░░▒▒▐▒▒░░░░░░░▌\n▐▒░░░░░▒▒▒▐▒▒▒░░░░░▒▌\n.▀▄▒▒▒▒▒▄▀▒▀▄▒▒▒▒▒▄▀\n.. ▀▀▀▀▀ ▀▀▀▀▀']

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i %25 ])
