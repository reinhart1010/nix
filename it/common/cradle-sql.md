---
layout: page
title: common/cradle-sql (italiano)
description: "Gestisci database SQL di Cradle."
content_hash: ff7eec86659ba50d9e7be8ab71a6f39af8d4c495
related_topics:
  - title: Deutsch version
    url: /de/common/cradle-sql.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/cradle-sql.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cradle-sql.html
    icon: bi bi-globe
---
# cradle sql

Gestisci database SQL di Cradle.
Maggiori informazioni: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql>.

- Ricostruisci lo schema del database:

`cradle sql build`

- Ricostruisci lo schema del database per uno specifico pacchetto:

`cradle sql build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacchetto</span>

- Svuota l'intero database:

`cradle sql flush`

- Svuota le tabelle del database per uno specifico pacchetto:

`cradle sql flush `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacchetto</span>

- Popola le tabelle per tutti i pacchetti:

`cradle sql populate`

- Popola le tabelle per uno specifico pacchetto:

`cradle sql populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome_pacchetto</span>
