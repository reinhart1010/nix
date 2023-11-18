---
layout: page
title: windows/choco-list (Nederlands)
description: "Toon een lijst van pakketten met Chocolatey."
content_hash: 621eb07b1b7d3f0f15ec072d48a6e013e3caff55
last_modified_at: 2023-11-18
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
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/windows/choco-list.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># choco list

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

`choco list --source `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">source_url|alias</span>

- Geef een gebruikersnaam en wachtwoord voor authenticatie op:

`choco list --user `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">username</span>` --password `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">password</span>
