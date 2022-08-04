---
layout: page
title: common/cradle-sql (Deutsch)
description: "Verwalte Cradle SQL Datenbanken."
content_hash: 67b4f93ab228fafcba542f8a1ebba01ed5e9cc3f
related_topics:
  - title: English version
    url: /en/common/cradle-sql.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/cradle-sql.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/cradle-sql.html
    icon: bi bi-globe
---
# cradle sql

Verwalte Cradle SQL Datenbanken.
Weitere Informationen: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#sql>.

- Generiere ein neues Datenbank-Schema:

`cradle sql build`

- Generiere ein neues Datenbank-Schema für ein bestimmtes Paket:

`cradle sql build `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Entleere die gesamte Datenbank:

`cradle sql flush`

- Entleere die Datenbank für ein bestimmtes Paket:

`cradle sql flush `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>

- Befülle die Tabellen für alle Pakete:

`cradle sql populate`

- Befülle die Tabellen für ein bestimmtes Paket:

`cradle sql populate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paket</span>
