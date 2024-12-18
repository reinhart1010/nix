---
layout: page
title: common/pgrep (español)
description: "Encuentra o envía una señal a procesos por nombre."
content_hash: 44d80e05e45f760673972bf22ad766827a71d920
last_modified_at: 2024-12-18
related_topics:
  - title: English version
    url: /en/common/pgrep.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/pgrep.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pgrep

Encuentra o envía una señal a procesos por nombre.
Más información: <https://www.manned.org/pgrep>.

- Regresa PIDs de cualquier proceso de ejecución con una cadena de comando que coincida:

`pgrep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_proceso</span>

- Busca procesos incluyendo sus opciones de línea de comandos:

`pgrep --full "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_proceso</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">parámetro</span>`"`

- Busca procesos gestionados por un usuario específico:

`pgrep --euid root `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_proceso</span>
