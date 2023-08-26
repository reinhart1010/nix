---
layout: page
title: linux/cpulimit (català)
description: "Eina per limitar l'ús de la CPU en altres processos."
content_hash: 2b76a7e5994b4ff62de955d750702dfe8edb071a
last_modified_at: 2023-08-26
related_topics:
  - title: English version
    url: /en/linux/cpulimit.html
    icon: bi bi-globe
  - title: español version
    url: /es/linux/cpulimit.html
    icon: bi bi-globe
---
# cpulimit

Eina per limitar l'ús de la CPU en altres processos.
Més informació: <http://cpulimit.sourceforge.net/>.

- Limita un procés existent amb PID 1234 perquè només utilitzi el 25% de CPU:

`cpulimit --pid `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1234</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25%</span>

- Limita un programa existent per el seu nom d'execució:

`cpulimit --exe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>` --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>

- Executa un programa determinat i limita el seu ús a només el 50% de la CPU:

`cpulimit --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa argument1 argument2 ...</span>

- Executa un programa, limita l'ús de la CPU a 50% i executa cpulimit en segon pla:

`cpulimit --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">50</span>` --background -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Mata el procés si l'ús de CPU del programa supera el 50%:

`cpulimit --limit 50 --kill -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>

- Regula el seu procés i els subprocessos perquè cap superi el 25% de CPU:

`cpulimit --limit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">25</span>` --monitor-forks -- `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">programa</span>
