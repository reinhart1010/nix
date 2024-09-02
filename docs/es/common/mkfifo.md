---
layout: page
title: common/mkfifo (español)
description: "Crea FIFOs (llamadas pipes)."
content_hash: b7f8a00e00004ad939317459c5988d60d972abc8
last_modified_at: 2024-09-02
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
tldri18n_status: 2
---
# mkfifo

Crea FIFOs (llamadas pipes).
Más información: <https://www.gnu.org/software/coreutils/mkfifo>.

- Crea un pipe con nombre en una ruta dada:

`mkfifo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/pipe</span>

- Envía datos a través de un pipe con nombre y envía el comando al fondo:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">"Hola Mundo"</span>` > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/pipe</span>` &`

- Recibe datos a través de un pipe con nombre:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/pipe</span>
