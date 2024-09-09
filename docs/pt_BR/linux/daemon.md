---
layout: page
title: linux/daemon (português (Brasil))
description: "Roda processos em daemons."
content_hash: bd1819e44141fb197bb28ff88f96cbb9809cd67f
last_modified_at: 2024-09-09
related_topics:
  - title: English version
    url: /en/linux/daemon.html
    icon: bi bi-globe
tldri18n_status: 2
---
# daemon

Roda processos em daemons.
Mais informações: <https://manned.org/daemon>.

- Roda um comando como um daemon:

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>`" `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Roda um comando como um daemon que será reiniciado se o comando falhar:

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>`" --respawn `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Roda um comando como um daemon que será reiniciado se falar, com duas tentativas a cada 10 segundos:

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>`" --respawn --attempts=2 --delay=10 `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Roda um comando como um daemon, gravando registros em um arquivo específico:

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>`" --errlog=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">caminho/para/arquivo.log</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>

- Elimina um daemon (SIGTERM):

`daemon --name="`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nome</span>`" --stop`

- Lista os daemons:

`daemon --list`
