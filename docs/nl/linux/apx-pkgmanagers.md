---
layout: page
title: linux/apx-pkgmanagers (Nederlands)
description: "Beheer pakketmanagers in `apx`."
content_hash: a027811d21fc465be5ff9a15b32cdcfcfab0b277
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/linux/apx-pkgmanagers.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apx pkgmanagers

Beheer pakketmanagers in `apx`.
Let op: Door gebruikers gecreëerde pakketbeheerderconfiguraties worden opgeslagen in `~/.local/share/apx/pkgmanagers`.
Meer informatie: <https://github.com/Vanilla-OS/apx>.

- Maak interactief een nieuwe configuratie voor een pakketbeheerder:

`apx pkgmanagers create`

- Toon alle beschikbare pakketbeheerderconfiguraties:

`apx pkgmanagers list`

- Verwijder een configuratie van een pakketbeheerder:

`apx pkgmanagers rm --name `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">string</span>

- Geef informatie weer over een specifieke pakketbeheerder:

`apx pkgmanagers show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">name</span>
