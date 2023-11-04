---
layout: page
title: common/while (português (Brasil))
description: "Loop simples da shell."
content_hash: ce62a23175da9886ae54de85c0e76ccab88e6bd9
last_modified_at: 2023-11-04
related_topics:
  - title: English version
    url: /en/common/while.html
    icon: bi bi-globe
---
# while

Loop simples da shell.
Mais informações: <https://manned.org/while>.

- Lê a entrada default (`stdin`) e realiza uma ação a cada linha:

`while read line; do echo "$line"; done`

- Executa um comando para sempre a cada segundo:

`while :; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`; sleep 1; done`
