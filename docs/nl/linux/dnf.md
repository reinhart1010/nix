---
layout: page
title: linux/dnf (Nederlands)
description: "Hulpprogramma voor pakketbeheer van RHEL, Fedora en CentOS (vervangt Yum)."
content_hash: ecf8279c4125386962dd8ed0320528744ebb904b
last_modified_at: 2025-01-03
related_topics:
  - title: català version
    url: /ca/linux/dnf.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/dnf.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/dnf.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/dnf.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/dnf.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/linux/dnf.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/dnf.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/dnf.html
    icon: bi bi-globe
  - title: தமிழ் version
    url: /ta/linux/dnf.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/dnf.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/dnf.html
    icon: bi bi-globe
tldri18n_status: 2
---
# dnf

Hulpprogramma voor pakketbeheer van RHEL, Fedora en CentOS (vervangt Yum).
Voor gelijkwaardige commando's binnen andere pakketbeheer, zie <https://wiki.archlinux.org/title/Pacman/Rosetta>.
Meer informatie: <https://dnf.readthedocs.io>.

- Upgrade geïnstalleerde pakketten naar de nieuwste beschikbare versies:

`sudo dnf upgrade`

- Zoek naar pakketten via sleutelwoorden:

`dnf search `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sleutelwoord1 sleutelwoord2 ...</span>

- Toon gedetailleerde informatie over een pakket:

`dnf info `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket</span>

- Installeer nieuwe pakketten (gebruik `-y` om alle prompts automatisch te bevestigen):

`sudo dnf install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket1 pakket2 ...</span>

- Verwijder een pakket:

`sudo dnf remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket1 pakket2 ...</span>

- Toon alle geïnstalleerde pakketten:

`dnf list --installed`

- Vind welk pakket voorziet van een bepaald commando:

`dnf provides `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>

- Toon alle historische operaties:

`dnf history`
