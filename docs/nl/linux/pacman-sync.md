---
layout: page
title: linux/pacman-sync (Nederlands)
description: "Hulpprogramma voor het beheren van pakketten op Arch Linux."
content_hash: 71a67468a552a0ed0d94d968cf4be82f5ade6f24
last_modified_at: 2025-03-02
related_topics:
  - title: Deutsch version
    url: /de/linux/pacman-sync.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/pacman-sync.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/pacman-sync.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/pacman-sync.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pacman-sync.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/pacman-sync.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/pacman-sync.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/pacman-sync.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pacman --sync

Hulpprogramma voor het beheren van pakketten op Arch Linux.
Bekijk ook: `pacman`.
Meer informatie: <https://manned.org/pacman.8>.

- Installeer een nieuw pakket:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- [S]ynchroniseer en ververs ([y]) de pakketdatabase en voer een sys[u]pgrade uit (voeg `--downloadonly` toe om alleen de pakketten te downloaden en niet te upgraden):

`sudo pacman -Syu`

- Update en [u]pgrade alle pakketten en installeer een nieuw pakket zonder bevestiging:

`sudo pacman -Syu --noconfirm `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Doorzoek ([s]) de pakketdatabase met een reguliere expressie of zoekwoord:

`pacman -Ss "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">zoekterm</span>`"`

- Toon [i]nformatie over een pakket:

`pacman -Si `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Overschrijf conflicterende bestanden tijdens een pakketupdate:

`sudo pacman -Syu --overwrite `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>

- Verwijder niet-geïnstalleerde pakketten en ongebruikte repositories uit de cache (gebruik de vlag `Sc` om [c]ache volledig schoon te maken):

`sudo pacman -Sc`

- Specificeer de pakketversie die geïnstalleerd dient te worden:

`sudo pacman -S `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">versie</span>
