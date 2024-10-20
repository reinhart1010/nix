---
layout: page
title: windows/rpcinfo (Nederlands)
description: "Toon programma's via RPC op externe computers."
content_hash: 67a8e9a2c4852b41910272f9ede81f9f64c9e31f
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/windows/rpcinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rpcinfo

Toon programma's via RPC op externe computers.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/rpcinfo>.

- Toon alle programma's geregistreerd op de lokale computer:

`rpcinfo`

- Toon alle programma's geregistreerd op een externe computer:

`rpcinfo /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_naam</span>

- Roep een specifiek programma aan op een externe computer via TCP:

`rpcinfo /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma_naam</span>

- Roep een specifiek programma aan op een externe computer via UDP:

`rpcinfo /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma_naam</span>
