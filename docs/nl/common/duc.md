---
layout: page
title: common/duc (Nederlands)
description: "Een verzameling van tools voor het indexeren, inspecteren en visualiseren van schijfgebruik."
content_hash: e9c140aef19c1a87493c3f7c7136fd9630aa042e
last_modified_at: 2024-10-20
related_topics:
  - title: English version
    url: /en/common/duc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/duc.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/duc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# duc

Een verzameling van tools voor het indexeren, inspecteren en visualiseren van schijfgebruik.
Duc onderhoudt een database van geaccumuleerde groottes van directories van het bestandssysteem, waardoor je deze database kunt raadplegen of mooie grafieken kunt maken om te laten zien waar de data zich bevindt.
Meer informatie: <http://duc.zevv.nl>.

- Indexeer de /usr directory en schrijf naar de standaard database locatie ~/.duc.db:

`duc index `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Toon alle bestanden en directories onder /usr/local en toon relatieve bestandsgroottes in een [g]rafiek:

`duc ls -Fg `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- Toon alle bestanden en directories onder /usr/local recursief met behulp van boomweergave:

`duc ls -Fg -R `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr/local</span>

- Start de grafische interface om het bestandssysteem te verkennen met behulp van zonnestraalgrafieken:

`duc gui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Start de ncurses console interface om het bestandssysteem te verkennen:

`duc ui `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">/usr</span>

- Dump database-informatie:

`duc info`
