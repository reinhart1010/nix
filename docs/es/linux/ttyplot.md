---
layout: page
title: linux/ttyplot (español)
description: "Una utilidad de trazado en tiempo real para la línea de comandos con entrada de datos desde `stdin`."
content_hash: 9804d36ef5ac057ccb9e37c82504aeaeb763e379
last_modified_at: 2024-12-21
related_topics:
  - title: English version
    url: /en/linux/ttyplot.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/ttyplot.html
    icon: bi bi-globe
tldri18n_status: 2
---
# ttyplot

Una utilidad de trazado en tiempo real para la línea de comandos con entrada de datos desde `stdin`.
Más información: <https://github.com/tenox7/ttyplot>.

- Muestra los valores `1`, `2` y `3` (`cat` evita que ttyplot salga):

`{ echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1 2 3</span>`; cat } | ttyplot`

- Establece un título específico y unidad:

`{ echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1 2 3</span>`; cat } | ttyplot -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">título</span>` -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">unidad</span>

- Utiliza un bucle de tiempo para trazar continuamente valores aleatorios:

`{ while `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">true</span>`; do echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">$RANDOM</span>`; sleep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1</span>`; done } | ttyplot`

- Analiza la salida de `ping` y la visualiza:

`ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">8.8.8.8</span>` | sed -u '`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">s/^.*time=//g; s/ ms//g</span>`' | ttyplot -t "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ping a 8.8.8.8</span>`" -u `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ms</span>
