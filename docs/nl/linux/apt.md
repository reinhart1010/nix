---
layout: page
title: linux/apt (Nederlands)
description: "Hulpprogramma voor pakketbeheer voor op Debian gebaseerde distributies."
content_hash: e409b538f54a9ea962e47372c2e405afa33418b7
last_modified_at: 2024-09-18
related_topics:
  - title: العربية version
    url: /ar/linux/apt.html
    icon: bi bi-globe
  - title: বাংলা version
    url: /bn/linux/apt.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/linux/apt.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/apt.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/linux/apt.html
    icon: bi bi-globe
  - title: മലയാളം version
    url: /ml/linux/apt.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/linux/apt.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/apt.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt

Hulpprogramma voor pakketbeheer voor op Debian gebaseerde distributies.
Aanbevolen vervanging voor `apt-get` bij interactief gebruik in Ubuntu versie 16.04 en later.
Voor gelijkwaardige commando's in andere pakket managers, zie <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Meer informatie: <https://manned.org/apt.8>.

- Werk de lijst van beschikbare pakketten en versies bij (het wordt aanbevolen dit uit te voeren voor elk ander `apt` commando):

`sudo apt update`

- Zoek naar een specifiek pakket:

`apt search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Toon informatie voor een specifiek pakket:

`apt show `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket1 pakket2 ...</span>

- Installeer specifieke pakketten of werk ze bij naar de nieuwste beschikbare versies:

`sudo apt install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket1 pakket2 ...</span>

- Verwijder specifieke pakketten (gebruik in plaats daarvan purge om ook hun configuratiebestanden te verwijderen):

`sudo apt remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket1 pakket2 ...</span>

- Upgrade alle geïnstalleerde pakketten naar hun nieuwste beschikbare versies:

`sudo apt upgrade`

- Maak een lijst van alle pakketten:

`apt list`

- Maak een lijst van alle geïnstalleerde pakketten:

`apt list --installed`
