---
layout: page
title: common/finger (Nederlands)
description: "Programma voor het opzoeken van gebruikersinformatie."
content_hash: 1bb6710ae7b717216264fc02bbdee59c750d2385
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/common/finger.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/finger.html
    icon: bi bi-globe
tldri18n_status: 2
---
# finger

Programma voor het opzoeken van gebruikersinformatie.
Meer informatie: <https://manned.org/finger>.

- Toon informatie over momenteel ingelogde gebruikers:

`finger`

- Toon informatie over een specifieke gebruiker:

`finger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Toon de loginnaam, echte naam, terminalnaam en andere informatie van de gebruiker:

`finger -s`

- Geef een output in meerdere regels weer met dezelfde informatie als `-s` evenals de thuisdirectory van de gebruiker, thuistelefoonnummer, loginshell, mailstatus, enz.:

`finger -l`

- Voorkom het matchen tegen gebruikersnamen en gebruik alleen login namen:

`finger -m`
