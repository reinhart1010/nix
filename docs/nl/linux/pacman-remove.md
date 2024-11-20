---
layout: page
title: linux/pacman-remove (Nederlands)
description: "Hulpprogramma voor het beheren van pakketten op Arch Linux."
content_hash: c159d2806f128428963e5251e898e324859327d2
last_modified_at: 2024-11-20
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-remove.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-remove.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-remove.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-remove.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-remove.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-remove.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-remove.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --remove

Hulpprogramma voor het beheren van pakketten op Arch Linux.
Bekijk ook: `pacman`.
Meer informatie: <https://manned.org/pacman.8>.

- Verwijde[R] een pakket en zijn afhankelijkheden recur[s]ief:

`sudo pacman -Rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Verwijde[R] een pakket en zijn afhankelijkheden. Maak ook gee[n] back-ups van configuratiebestanden:

`sudo pacman -Rsn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Verwijde[R] een pakket zonder bevestigingsprompt:

`sudo pacman -R --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Verwijde[R] weespakketten (geïnstalleerd als [d]ependencies maar [n]iet vereist door een ander pakket):

`sudo pacman -Rsn $(pacman -Qdtq)`

- Verwijde[R] een pakket en [c]ascadeer dat naar alle pakketten die ervan afhankelijk zijn:

`sudo pacman -Rc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Toon en [p]rint pakketten die beïnvloed zouden worden (verwijdert [R] geen pakketten):

`pacman -Rp `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Toon [h]ulp:

`pacman -Rh`
