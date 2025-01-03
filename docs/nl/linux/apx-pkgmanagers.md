---
layout: page
title: linux/apx-pkgmanagers (Nederlands)
description: "Beheer pakketmanagers in `apx`."
content_hash: c4f168cd1c55b552a3bc44f3d91bc21f360ed14b
last_modified_at: 2025-01-03
related_topics:
  - title: English version
    url: /en/linux/apx-pkgmanagers.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/apx-pkgmanagers.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apx pkgmanagers

Beheer pakketmanagers in `apx`.
Let op: door gebruikers gecreëerde pakketbeheerconfiguraties worden opgeslagen in `~/.local/share/apx/pkgmanagers`.
Meer informatie: <https://github.com/Vanilla-OS/apx>.

- Maak interactief een nieuwe configuratie voor een pakketbeheer:

`apx pkgmanagers create`

- Toon alle beschikbare pakketbeheerconfiguraties:

`apx pkgmanagers list`

- Verwijder een configuratie van een pakketbeheer:

`apx pkgmanagers rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- Geef informatie weer over een specifieke pakketbeheer:

`apx pkgmanagers show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
