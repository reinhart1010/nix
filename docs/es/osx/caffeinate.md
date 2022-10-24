---
layout: page
title: osx/caffeinate (español)
description: "Evita que macOS entre en modo de reposo."
content_hash: 9016d83c53ba206fb6bd5d8cface0fd4e74b24c2
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
  - title: português (Brasil) version
    url: /pt_BR/osx/caffeinate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/caffeinate.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># caffeinate

Evita que macOS entre en modo de reposo.
Más información: <https://ss64.com/osx/caffeinate.html>.

- Evita entrar en modo reposo por 1 hora (3600 segundos):

`caffeinate -u -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Evita entrar en modo reposo hasta que un comando finaliza:

`caffeinate -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">command</span>`"`

- Evita entrar en modo reposo (use `Ctrl + C` para salir):

`caffeinate -i`

- Evita al disco entrar en modo reposo (use `Ctrl + C` para salir):

`caffeinate -m`
