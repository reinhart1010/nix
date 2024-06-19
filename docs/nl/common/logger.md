---
layout: page
title: common/logger (Nederlands)
description: "Voeg berichten toe aan syslog (/var/log/syslog)."
content_hash: a18533dd17ebdc63d82bd5f5b7b5ad8fdc31d269
last_modified_at: 2024-06-19
related_topics:
  - title: English version
    url: /en/common/logger.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/logger.html
    icon: bi bi-globe
tldri18n_status: 2
---
# logger

Voeg berichten toe aan syslog (/var/log/syslog).
Meer informatie: <https://manned.org/logger>.

- Log een bericht naar syslog:

`logger `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">bericht</span>

- Neem invoer van `stdin` en log naar syslog:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">log_entry</span>` | logger`

- Stuur de uitvoer naar een externe syslog-server die op een bepaalde poort draait. Standaardpoort is 514:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">log_entry</span>` | logger --server `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">hostname</span>` --port `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">poort</span>

- Gebruik een specifieke tag voor elke gelogde regel. Standaard is de naam van de ingelogde gebruiker:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">log_entry</span>` | logger --tag `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">tag</span>

- Log berichten met een gegeven prioriteit. Standaard is `user.notice`. Zie `man logger` voor alle prioriteitsopties:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">log_entry</span>` | logger --priority `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">user.warning</span>
