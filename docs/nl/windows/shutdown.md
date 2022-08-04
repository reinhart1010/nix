---
layout: page
title: windows/shutdown (Nederlands)
description: "Een tool om een machine af te sluiten, her op te starten of af te melden."
content_hash: 4fd54f86446c08fdd7767a92fc17e6d5649ebdec
related_topics:
  - title: English version
    url: /en/windows/shutdown.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/shutdown.html
    icon: bi bi-globe
---
# shutdown

Een tool om een machine af te sluiten, her op te starten of af te melden.
Meer informatie: <https://docs.microsoft.com/windows-server/administration/windows-commands/shutdown>.

- Sluit de huidige machine af:

`shutdown /s`

- Sluit de huidige machine af en sluit alle applicaties:

`shutdown /s /f`

- Herstart de huidige machine:

`shutdown /r /t 0`

- Zet de huidige machine in slaapstand:

`shutdown /h`

- Log uit van de huidige machine:

`shutdown /l`

- Zet een timer in aantal seconden voor het afsluiten van de huidige machine:

`shutdown /s /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">seconden</span>

- Breek een afsluit sequentie af vooraleer de timer was afgelopen:

`shutdown /a`

- Sluit een machine af op afstand:

`shutdown /m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">\\hostnaam</span>
