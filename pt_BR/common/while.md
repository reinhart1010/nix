---
layout: page
title: common/while (português (Brasil))
description: "Loop simples da shell."
content_hash: 8a3ff8ad0b30e68c36920d4f80e709588607cb3c
related_topics:
  - title: English version
    url: /en/common/while.html
    icon: bi bi-globe
---
# while

Loop simples da shell.

- Lê a entrada default (stdin) e realiza uma ação a cada linha:

`while read line; do echo "$line"; done`

- Executa um comando para sempre a cada segundo:

`while :; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`; sleep 1; done`
