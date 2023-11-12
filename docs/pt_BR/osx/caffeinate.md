---
layout: page
title: osx/caffeinate (português (Brasil))
description: "Evita que o macOS entre em suspensão (repouso)."
content_hash: 55d6c61c9348c87444f14bfbfd0d581b337ce09e
last_modified_at: 2023-11-12
related_topics:
  - title: Deutsch version
    url: /de/osx/caffeinate.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/caffeinate.html
    icon: bi bi-globe
  - title: español version
    url: /es/osx/caffeinate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/caffeinate.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/caffeinate.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/caffeinate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/caffeinate.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># caffeinate

Evita que o macOS entre em suspensão (repouso).
Mais informações: <https://ss64.com/osx/caffeinate.html>.

- Evita a suspensão por uma hora (3600 segundos):

`caffeinate -u -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Evita a suspensão até que um comando seja concluído:

`caffeinate -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Evita a suspensão até que você digite Ctrl-C:

`caffeinate -i`
