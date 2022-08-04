---
layout: page
title: osx/caffeinate (português (Brasil))
description: "Evita que o macOS entre em suspensão (repouso)."
content_hash: 55d6c61c9348c87444f14bfbfd0d581b337ce09e
related_topics:
  - title: Deutsch version
    url: /de/osx/caffeinate.html
    icon: bi bi-globe
  - title: English version
    url: /en/osx/caffeinate.html
    icon: bi bi-globe
  - title: Indonesia version
    url: /id/osx/caffeinate.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/osx/caffeinate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/caffeinate.html
    icon: bi bi-globe
---
# caffeinate

Evita que o macOS entre em suspensão (repouso).
Mais informações: <https://ss64.com/osx/caffeinate.html>.

- Evita a suspensão por uma hora (3600 segundos):

`caffeinate -u -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Evita a suspensão até que um comando seja concluído:

`caffeinate -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Evita a suspensão até que você digite Ctrl-C:

`caffeinate -i`
