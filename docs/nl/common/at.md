---
layout: page
title: common/at (Nederlands)
description: "Voer commando's eenmaal later uit."
content_hash: 48b1dbd49d21a79a6dcb797d06752411e4bdd33e
last_modified_at: 2024-08-13
related_topics:
  - title: English version
    url: /en/common/at.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/at.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/at.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/at.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/at.html
    icon: bi bi-globe
  - title: नेपाली version
    url: /ne/common/at.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/at.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/at.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/at.html
    icon: bi bi-globe
tldri18n_status: 2
---
# at

Voer commando's eenmaal later uit.
De service atd (of atrun) moet actief zijn voor de daadwerkelijke uitvoering.
Meer informatie: <https://manned.org/at>.

- Voer commando's uit van `stdin` over 5 minuten (druk op `Ctrl + D` als je klaar bent):

`at now + 5 minutes`

- Voer een commando uit van `stdin` om 10:00 AM vandaag:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./make_db_backup.sh</span>`" | at 1000`

- Voer commando's uit van een gegeven bestand volgende dinsdag:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` 9:30 PM Tue`
