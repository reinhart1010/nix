---
layout: page
title: linux/pacman-files (Nederlands)
description: "Arch Linux Pakketbeheerder hulpprogramma."
content_hash: 758df211ba41eab348b0f447f2de315db16f9770
last_modified_at: 2025-01-02
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-files.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-files.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/pacman-files.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-files.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-files.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-files.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/pacman-files.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-files.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --files

Arch Linux Pakketbeheerder hulpprogramma.
Bekijk ook: `pacman`,` pkgfile`.
Meer informatie: <https://manned.org/pacman.8>.

- Werk de pakketdatabase bij:

`sudo pacman -Fy`

- Zoek het pakket dat een specifiek bestand ([F]) bezit:

`pacman -F `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>

- Zoek het pakket dat een specifiek bestand ([F]) bezit, met behulp van een reguliere e[x]pressie:

`pacman -Fx '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">reguliere_expressie</span>`'`

- Maak een lijst van alleen de pakketnamen:

`pacman -Fq `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bestandsnaam</span>

- Toon ([l]) de bestanden ([F]) die eigendom zijn van een specifiek pakket:

`pacman -Fl `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Toon de [h]elp:

`pacman -Fh`
