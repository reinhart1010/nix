---
layout: page
title: linux/duc (Nederlands)
description: "Een verzameling tools voor het indexeren, inspecteren en visualiseren van schijfgebruik."
content_hash: ae5c71ed7368650260f9233f9cd1e3a98f33c74c
last_modified_at: 2024-08-14
related_topics:
  - title: English version
    url: /en/linux/duc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# duc

Een verzameling tools voor het indexeren, inspecteren en visualiseren van schijfgebruik.
Duc onderhoudt een database van geaccumuleerde groottes van directories in het bestandssysteem, waardoor je deze database kunt raadplegen of mooie grafieken kunt maken om te laten zien waar de data zich bevindt.
Meer informatie: <https://duc.zevv.nl/>.

- Indexeer de `/usr` directory en schrijf naar de standaard database locatie `~/.duc.db`:

`duc index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Lijst alle bestanden en directories onder `/usr/local` en toon relatieve bestandsgroottes in een [g]rafiek:

`duc ls --classify --graph `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- Lijst alle bestanden en directories onder `/usr/local` recursief met behulp van boomweergave:

`duc ls --classify --graph --recursive `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- Start de grafische interface om het bestandssysteem te verkennen met behulp van zonnestraalgrafieken:

`duc gui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Start de ncurses console interface om het bestandssysteem te verkennen:

`duc ui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Dump database-informatie:

`duc info`
