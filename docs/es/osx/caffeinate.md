---
layout: page
title: osx/caffeinate (español)
description: "Evita que macOS se duerma."
content_hash: 7c99c2dac7d39eabecd9e980851300f156c3b355
last_modified_at: 2024-10-11
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
  - title: Nederlands version
    url: /nl/osx/caffeinate.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/caffeinate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/osx/caffeinate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/caffeinate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# caffeinate

Evita que macOS se duerma.
Más información: <https://keith.github.io/xcode-man-pages/caffeinate.8.html>.

- Evita que macOS entre en reposo durante 1 hora (3600 segundos):

`caffeinate -u -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">3600</span>

- Evita que entre en reposo hasta que termine de ejecutarse un comando:

`caffeinate -s "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comando</span>`"`

- Evita que el sistema entre en reposo hasta que finalice un proceso con el PID especificado:

`caffeinate -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pid</span>

- Evita que entre en reposo (usa `Ctrl + C` para salir):

`caffeinate -i`

- Evita que el disco entre en reposo (usa `Ctrl + C` para salir):

`caffeinate -m`
