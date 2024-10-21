---
layout: page
title: common/at (Nederlands)
description: "Voer commando's één keer uit op een later tijdstip."
content_hash: 98352049ab3549a5f25561e75d1f7c46c10a4670
last_modified_at: 2024-10-21
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

Voer commando's één keer uit op een later tijdstip.
Resultaten worden naar de e-mail van de gebruiker gestuurd.
Meer informatie: <https://manned.org/at>.

- Start de `atd`-daemon:

`systemctl start atd`

- Maak commando's interactief en voer ze over 5 minuten uit (druk op `<Ctrl> + D` wanneer klaar):

`at now + 5 minutes`

- Maak commando's interactief en voer ze uit op een specifiek tijdstip:

`at `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">uu:mm</span>

- Voer een commando uit vanuit `stdin` om 10:00 uur vandaag:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">commando</span>`" | at 1000`

- Voer commando's uit vanuit een opgegeven bestand volgende dinsdag:

`at -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pad/naar/bestand</span>` 9:30 PM Tue`
