---
layout: page
title: common/act (español)
description: "Ejecuta acciones de GitHub localmente mediante Docker."
content_hash: 0a9eb3f8f2ec5c4558e9e4e95e365e7347c1be4f
last_modified_at: 2024-05-22
related_topics:
  - title: English version
    url: /en/common/act.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/act.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/act.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/act.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/act.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/act.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/act.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/act.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># act

Ejecuta acciones de GitHub localmente mediante Docker.
Más información: <https://github.com/nektos/act>.

- Lista las acciones disponibles:

`act -l`

- Ejecuta el evento por defecto:

`act`

- Ejecuta un evento específico:

`act `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">event_type</span>

- Ejecuta una acción específica:

`act -a `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">identificador_de_acción</span>

- Simula una acción:

`act -n`

- Muestra registros detallados:

`act -v`
