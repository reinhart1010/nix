---
layout: page
title: common/atq (español)
description: "Muestra trabajos programados por comandos `at` o `batch`."
content_hash: b3d62ca28e9d72fc80f05816012308e6b426bf30
last_modified_at: 2024-12-19
related_topics:
  - title: English version
    url: /en/common/atq.html
    icon: bi bi-globe
  - title: فارسی version
    url: /fa/common/atq.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atq.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atq.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atq.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/atq.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/atq.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># atq

Muestra trabajos programados por comandos `at` o `batch`.
Más información: <https://manned.org/atq>.

- Muestra los trabajos programados del usuario actual:

`atq`

- Muestra trabajos de la 'a' [q]ueue (las colas tienen nombres de caracteres individuales):

`atq -q `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">a</span>

- Muestra trabajos de todos los usuarios (ejecuta como superusuario):

`sudo atq`
