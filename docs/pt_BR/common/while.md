---
layout: page
title: common/while (português (Brasil))
description: "Loop simples da shell."
content_hash: 7ea2724da06689c0cc8e7268967ae67f615e225f
related_topics:
  - title: English version
    url: /en/common/while.html
    icon: bi bi-globe
---
# while

Loop simples da shell.
Mais informações: <https://manned.org/while>.

- Lê a entrada default (stdin) e realiza uma ação a cada linha:

`while read line; do echo "$line"; done`

- Executa um comando para sempre a cada segundo:

`while :; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`; sleep 1; done`
