---
layout: page
title: common/history (português (Portugal))
description: "Histórico da linha de comandos."
content_hash: 23a7f619c6bc6cdeb132532c976dd32e43f136ef
related_topics:
  - title: English version
    url: /en/common/history.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/history.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/history.html
    icon: bi bi-globe
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/history.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># history

Histórico da linha de comandos.
Mais informações: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- Mostrar o histórico da linha de comandos por ordem cronológica:

`history`

- Apagar o histórico da linha de comandos:

`history -c`

- Mostrar o enésimo comando no histórico da linha de comandos:

`history !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Mostrar as entradas do histórico da linha de comandos que correspondem a uma expressão regular:

`history | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressao_regular</span>
