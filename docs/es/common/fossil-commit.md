---
layout: page
title: common/fossil-commit (español)
description: "Envía archivos a un repositorio Fossil."
content_hash: 95756497a4290b18306b4391f3bf2292153a1543
last_modified_at: 2024-11-17
related_topics:
  - title: English version
    url: /en/common/fossil-commit.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/fossil-commit.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/fossil-commit.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/fossil-commit.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/fossil-commit.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># fossil commit

Envía archivos a un repositorio Fossil.
Más información: <https://fossil-scm.org/home/help/commit>.

- Crea una nueva versión que contiene todos los cambios en el checkout actual; se solicitará al usuario un comentario:

`fossil commit`

- Crea una versión que contiene todos los cambios en el checkout actual, utilizando el comentario especificado:

`fossil commit --comment "`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">comentario</span>`"`

- Crea una versión que contiene todos los cambios en el checkout actual con un comentario leído de un archivo específico:

`fossil commit --message-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_con_comentario</span>

- Crea una versión que contiene cambios de los archivos especificados; se solicitará al usuario un comentario:

`fossil commit `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo1 ruta/al/archivo2 ...</span>
