---
layout: page
title: windows/rpcinfo (Nederlands)
description: "Lijst programma's via RPC op externe computers."
content_hash: b08d6169eae33a432264505d649b4a175ad84de2
last_modified_at: 2024-09-22
related_topics:
  - title: English version
    url: /en/windows/rpcinfo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# rpcinfo

Lijst programma's via RPC op externe computers.
Meer informatie: <https://learn.microsoft.com/windows-server/administration/windows-commands/rpcinfo>.

- Lijst alle programma's geregistreerd op de lokale computer:

`rpcinfo`

- Lijst alle programma's geregistreerd op een externe computer:

`rpcinfo /p `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_naam</span>

- Roep een specifiek programma aan op een externe computer via TCP:

`rpcinfo /t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma_naam</span>

- Roep een specifiek programma aan op een externe computer via UDP:

`rpcinfo /u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">computer_naam</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programma_naam</span>
