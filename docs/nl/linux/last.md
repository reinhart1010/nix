---
layout: page
title: linux/last (Nederlands)
description: "Toon informatie over de laatste gebruikerslogins."
content_hash: 7994f9951abb2e7b9b5e41bc170015d553335a2b
last_modified_at: 2024-08-21
related_topics:
  - title: English version
    url: /en/linux/last.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/last.html
    icon: bi bi-globe
tldri18n_status: 2
---
# last

Toon informatie over de laatste gebruikerslogins.
Bekijk ook: `lastb`, `login`.
Meer informatie: <https://manned.org/last.1>.

- Toon logininformatie (bijv. gebruikersnaam, terminal, opstarttijd, kernel) van alle gebruikers:

`last`

- Toon logininformatie van een specifieke gebruiker:

`last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>

- Toon informatie van een specifieke TTY:

`last `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tty1</span>

- Toon de meest recente informatie (standaard staan de nieuwste bovenaan):

`last | tac`

- Toon informatie over systeemopstarts:

`last "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">system boot</span>`"`

- Toon informatie met een specifiek [t]ijdstempel formaat:

`last --time-format `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">notime|full|iso</span>

- Toon informatie [s]inds een specifieke tijd en datum:

`last --since `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-7days</span>

- Toon informatie (bijv. hostnaam en IP) van externe hosts:

`last --dns`
