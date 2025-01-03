---
layout: page
title: linux/mesg (Nederlands)
description: "Controleer of stel in of een terminal berichten van andere gebruikers kan ontvangen, meestal van het `write`-commando."
content_hash: bd0b34a7a1fe4d9ff5d73b0bd99fe99bb37cbfd9
last_modified_at: 2025-01-03
related_topics:
  - title: English version
    url: /en/linux/mesg.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/mesg.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mesg

Controleer of stel in of een terminal berichten van andere gebruikers kan ontvangen, meestal van het `write`-commando.
Bekijk ook `write`, `talk`.
Meer informatie: <https://manned.org/mesg.1>.

- Controleer of de terminal openstaat voor berichten:

`mesg`

- Sta geen berichten toe van andere gebruikers:

`mesg n`

- Sta berichten toe van andere gebruikers:

`mesg y`

- Schakel [v]erbose modus in, en toon een waarschuwing als het commando niet wordt uitgevoerd vanaf een terminal:

`mesg --verbose`
