---
layout: page
title: linux/pacman-deptest (Nederlands)
description: "Controleer elke opgegeven afhankelijkheid en retourneer een lijst met afhankelijkheden die momenteel niet zijn voldaan op het systeem."
content_hash: 2a39223fdaab476c809a813aa7363cf19b656d5c
last_modified_at: 2025-01-04
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman-deptest.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-deptest.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --deptest

Controleer elke opgegeven afhankelijkheid en retourneer een lijst met afhankelijkheden die momenteel niet zijn voldaan op het systeem.
Bekijk ook: `pacman`.
Meer informatie: <https://manned.org/pacman.8>.

- Toon de pakket-namen van de afhankelijkheden welke niet geïnstalleerd zijn:

`pacman -T `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket1 pakket2 ...</span>

- Controleer of het geïnstalleerde pakket voldoet met de gegeven minimale versie:

`pacman -T "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>=5</span>`"`

- Controleer of een latere versie van een pakket is geïnstalleerd:

`pacman -T "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bash>5</span>`"`

- Toon de [h]elp:

`pacman -Th`
