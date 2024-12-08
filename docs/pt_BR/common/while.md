---
layout: page
title: common/while (português (Brasil))
description: "Loop simples da shell."
content_hash: 5de5356085606d270ffdb17e46189effc8995807
last_modified_at: 2024-12-08
related_topics:
  - title: English version
    url: /en/common/while.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/while.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># while

Loop simples da shell.
Mais informações: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_09_04_09>.

- Lê a entrada default (`stdin`) e realiza uma ação a cada linha:

`while read line; do echo "$line"; done`

- Executa um comando para sempre a cada segundo:

`while :; do `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`; sleep 1; done`
