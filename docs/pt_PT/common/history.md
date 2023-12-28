---
layout: page
title: common/history (português (Portugal))
description: "Histórico da linha de comandos."
content_hash: 3f66e630d0e587aa8efec8ea52a32216ad7fa0f5
last_modified_at: 2023-12-28
related_topics:
  - title: English version
    url: /en/common/history.html
    icon: bi bi-globe
  - title: español version
    url: /es/common/history.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/common/history.html
    icon: bi bi-globe
  - title: 日本語 version
    url: /ja/common/history.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/history.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/history.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># history

Histórico da linha de comandos.
Mais informações: <https://www.gnu.org/software/bash/manual/html_node/Bash-History-Builtins.html>.

- Mostra o histórico da linha de comandos por ordem cronológica:

`history`

- Apaga o histórico da linha de comandos:

`history -c`

- Mostra o enésimo comando no histórico da linha de comandos:

`history !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">n</span>

- Mostra as entradas do histórico da linha de comandos que correspondem a uma expressão regular:

`history | grep `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">expressao_regular</span>
