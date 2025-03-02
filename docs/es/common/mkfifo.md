---
layout: page
title: common/mkfifo (español)
description: "Crea FIFOs (named pipes) (pipes nombrados)."
content_hash: 9b52ef32552924a9154900f13db60677e727362a
last_modified_at: 2025-03-02
related_topics:
  - title: bosanski version
    url: /bs/common/mkfifo.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/mkfifo.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/mkfifo.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/mkfifo.html
    icon: bi bi-globe
tldri18n_status: 2
---
# mkfifo

Crea FIFOs (named pipes) (pipes nombrados).
Más información: <https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html>.

- Crea un pipe nombrado en una ruta específica:

`mkfifo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/pipe</span>

- Envía datos a través de un pipe nombrado ejecutando el comando en segundo plano:

`echo "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">Hola Mundo</span>`" > `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/pipe</span>` &`

- Recibe datos a través de un pipe nombrado:

`cat `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/pipe</span>

- Comparte tu sesión de la terminal en tiempo real:

`mkfifo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/pipe</span>`; script -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/pipe</span>
