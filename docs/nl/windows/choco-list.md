---
layout: page
title: windows/choco-list (Nederlands)
description: "Toon een lijst van pakketten met Chocolatey."
content_hash: 620549c0b30da9d742da49c52ad7ffb5f4570bc9
last_modified_at: 2024-05-09
related_topics:
  - title: Deutsch version
    url: /de/windows/choco-list.html
    icon: bi bi-globe
  - title: English version
    url: /en/windows/choco-list.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/windows/choco-list.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/windows/choco-list.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/windows/choco-list.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/windows/choco-list.html
    icon: bi bi-globe
tldri18n_status: 2
---
# choco list

Toon een lijst van pakketten met Chocolatey.
Meer informatie: <https://chocolatey.org/docs/commands-list>.

- Toon alle beschikbare pakketten:

`choco list`

- Toon alle lokaal geïnstalleerde pakketten:

`choco list --local-only`

- Toon een lijst inclusief lokale programma's:

`choco list --include-programs`

- Toon alleen goedgekeurde pakketten:

`choco list --approved-only`

- Geef een aangepaste bron op om pakketten van weer te geven:

`choco list --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bron_url|alias</span>

- Geef een gebruikersnaam en wachtwoord voor authenticatie op:

`choco list --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">gebruikersnaam</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">wachtwoord</span>
