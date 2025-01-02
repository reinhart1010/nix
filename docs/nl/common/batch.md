---
layout: page
title: common/batch (Nederlands)
description: "Voer commando's uit op een later tijdstip wanneer de systeembelasting het toelaat."
content_hash: 5173592c4d62cd47282a6328d6dc08a9606bfc0b
last_modified_at: 2025-01-02
related_topics:
  - title: English version
    url: /en/common/batch.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/batch.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/batch.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/batch.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/batch.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/batch.html
    icon: bi bi-globe
  - title: português (Portugal) version
    url: /pt_PT/common/batch.html
    icon: bi bi-globe
tldri18n_status: 2
---
# batch

Voer commando's uit op een later tijdstip wanneer de systeembelasting het toelaat.
Resultaten worden verzonden naar de e-mail van de gebruiker.
Bekijk ook: `at`, `atq`, `atrm` `mail`.
Meer informatie: <https://manned.org/batch>.

- Start de `atd` daemon:

`systemctl start atd`

- Voer commando's uit vanaf `stdin` (druk op `Ctrl + D` om te stoppen):

`batch`

- Voer een commando uit vanaf `stdin`:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">./make_db_backup.sh</span>`" | batch`
