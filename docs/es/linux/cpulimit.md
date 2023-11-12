---
layout: page
title: linux/cpulimit (español)
description: "Una herramienta para limitar el uso del CPU de otros procesos."
content_hash: 9cebe15a6e42bced9129fe88a4c052162c07cdc1
last_modified_at: 2023-11-12
related_topics:
  - title: català version
    url: /ca/linux/cpulimit.html
    icon: bi bi-globe
  - title: English version
    url: /en/linux/cpulimit.html
    icon: bi bi-globe
tldri18n_status: 2
---
# cpulimit

Una herramienta para limitar el uso del CPU de otros procesos.
Más información: <http://cpulimit.sourceforge.net/>.

- Limita un proceso existente con PID 1234 para que solo use el 25% del CPU:

`cpulimit --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25%</span>

- Limita un programa existente por su nombre de ejecución:

`cpulimit --exe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>

- Ejecuta un programa determinado y limita su uso a solo el 50% del CPU:

`cpulimit --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa argument1 argument2 ...</span>

- Ejecuta un programa, limita el uso del CPU a 50% y corre cpulimit en segundo plano:

`cpulimit --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` --background -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Mata su proceso si el uso del CPU del programa supera el 50%:

`cpulimit --limit 50 --kill -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Regula su proceso y sus subprocesos para que ninguno supere el 25% del CPU:

`cpulimit --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>` --monitor-forks -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>
