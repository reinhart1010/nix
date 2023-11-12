---
layout: page
title: linux/apt-get (Nederlands)
description: "Hulpprogramma voor pakketbeheer van Debian en Ubuntu."
content_hash: c80ad79ee2b43676f816fb67891c2dc7ca947186
last_modified_at: 2023-11-12
related_topics:
  - title: العربية version
    url: /ar/linux/apt-get.html
    icon: bi bi-globe
  - title: català version
    url: /ca/linux/apt-get.html
    icon: bi bi-globe
  - title: Deutsch version
    url: /de/linux/apt-get.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/apt-get.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/apt-get.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/linux/apt-get.html
    icon: bi bi-globe
  - title: français version
    url: /fr/linux/apt-get.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/linux/apt-get.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/linux/apt-get.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/linux/apt-get.html
    icon: bi bi-globe
  - title: Türkçe version
    url: /tr/linux/apt-get.html
    icon: bi bi-globe
  - title: українська version
    url: /uk/linux/apt-get.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/linux/apt-get.html
    icon: bi bi-globe
tldri18n_status: 2
---
# apt-get

Hulpprogramma voor pakketbeheer van Debian en Ubuntu.
Zoek naar pakketten met `apt-cache`.
Meer informatie: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Werk de lijst van beschikbare pakketten en versies bij (het wordt aanbevolen dit uit te voeren voor elk ander `apt-get` commando):

`apt-get update`

- Installeer specifieke pakketten of werk ze bij naar de nieuwste beschikbare versies:

`apt-get install `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket1 pakket2 ...</span>

- Verwijder specifieke pakketten:

`apt-get remove `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket1 pakket2 ...</span>

- Verwijder specifieke pakketten en hun configuratiebestanden:

`apt-get purge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pakket1 pakket2 ...</span>

- Upgrade alle geïnstalleerde pakketten naar hun nieuwste beschikbare versies:

`apt-get upgrade`

- Schoon de lokale repository op - verwijder pakketbestanden (`.deb`) van onderbroken downloads die niet langer kunnen worden gedownload:

`apt-get autoclean`

- Verwijder alle pakketten die niet meer nodig zijn:

`apt-get autoremove`

- Upgrade geïnstalleerde pakketten (zoals `upgrade`), maar verwijder verouderde pakketten en installeer aanvullende pakketten om aan nieuwe dependencies te voldoen:

`apt-get dist-upgrade`
