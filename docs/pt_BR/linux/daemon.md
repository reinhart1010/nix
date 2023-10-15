---
layout: page
title: linux/daemon (português (Brasil))
description: "Roda processos em daemons."
content_hash: b5175c261818ca974791a79346d3cb4ce464e2c4
last_modified_at: 2023-10-15
related_topics:
  - title: English version
    url: /en/linux/daemon.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># daemon

Roda processos em daemons.
Mais informações: <https://manned.org/man/daemon.1>.

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
