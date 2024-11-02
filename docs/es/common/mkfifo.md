---
layout: page
title: common/mkfifo (español)
description: "Crea FIFOs (named pipes) (pipes nombrados)."
content_hash: e9530ab59a3804e4854362530ad63f10d85b0e5d
last_modified_at: 2024-11-02
related_topics:
  - title: bosanski version
    url: /bs/common/mkfifo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/mkfifo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/mkfifo.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># mkfifo

Crea FIFOs (named pipes) (pipes nombrados).
Más información: <https://www.gnu.org/software/coreutils/mkfifo>.

- Crea un pipe nombrado en una ruta específica:

`mkfifo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/pipe</span>

- Envía datos a través de un pipe nombrado ejecutando el comando en segundo plano:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"Hola Mundo"</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/pipe</span>` &`

- Recibe datos a través de un pipe nombrado:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/pipe</span>

- Comparte tu sesión de la terminal en tiempo real:

`mkfifo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/pipe</span>`; script -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/pipe</span>
