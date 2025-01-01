---
layout: page
title: linux/pacman-query (Nederlands)
description: "Arch Linux pakketbeheerder hulpprogramma."
content_hash: f6139de0099a5b923f6c860f58477af3583a96ef
last_modified_at: 2025-01-01
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-query.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-query.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-query.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-query.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-query.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-query.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman-query.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-query.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pacman-query.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pacman --query

Arch Linux pakketbeheerder hulpprogramma.
Bekijk ook: `pacman`.
Meer informatie: <https://manned.org/pacman.8>.

- [Q]uery de lokale pakkettendatabase en toon geïnstalleerde pakketten en versies:

`pacman -Q`

- Toon alleen pakketten en versies welke [e]xpliciet geïnstalleerd zijn:

`pacman -Qe`

- Zoek welk pakket een bestand bezit ([o]):

`pacman -Qo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>

- Toon informatie over een geïnstalleerd ([i]) pakket:

`pacman -Qi `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Toon de [l]ijst met bestanden welke een specifiek pakket bezit:

`pacman -Ql `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Maak een lijst van pakketten welke geïnstalleerd zijn als afhankelijkhe[d]en maar niet vereist door een pakket en print in stille ([q]) modus (alleen pakketnaam wordt weergegeven):

`pacman -Qdtq`

- Toon geïnstalleerde pakketten foreign ([m]) voor de repository database:

`pacman -Qm`

- Toon pakketten die geüpgraded ([u]) kunnen worden:

`pacman -Qu`
