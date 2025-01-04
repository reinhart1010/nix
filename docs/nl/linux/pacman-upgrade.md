---
layout: page
title: linux/pacman-upgrade (Nederlands)
description: "Arch Linux pakketbeheer hulpprogramma."
content_hash: 75fce47e31c1ed42725e5cd62496db95d2d54ff0
last_modified_at: 2025-01-04
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-upgrade.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-upgrade.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --upgrade

Arch Linux pakketbeheer hulpprogramma.
Bekijk ook: `pacman`.
Meer informatie: <https://manned.org/pacman.8>.

- Installeer een of meerdere pakketten vanuit bestanden:

`sudo pacman -U `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakket1.pkg.tar.zst</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakket2.pkg.tar.zst</span>

- Installeer een pakket zonder vragen te stellen:

`sudo pacman -U --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakket.pkg.tar.zst</span>

- Overschrijf conflicterende bestanden tijdens het installeren van een pakket:

`sudo pacman -U --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakket.pkg.tar.zst</span>

- Installeer een pakket en sla de controles van afhankelijkhei[d]sversie over:

`sudo pacman -Ud `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakket.pkg.tar.zst</span>

- Haal pakketten op en toon ([p]) welke beïnvloed worden door een upgrade (installeert geen pakketten):

`pacman -Up `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/pakket.pkg.tar.zst</span>

- Toon de [h]elp:

`pacman -Uh`
