---
layout: page
title: common/alex (español)
description: "Una herramienta que detecta escritura insensible y desconsiderada."
content_hash: 9db99bd48326290f57c66660bd9593c9ebe57509
last_modified_at: 2023-01-04
related_topics:
  - title: English version
    url: /en/common/alex.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/alex.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/alex.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/alex.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/alex.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># alex

Una herramienta que detecta escritura insensible y desconsiderada.
Ayuda a encontrar en el texto frases que son parciales con el género, que polarizan, o están relacionadas con la raza, son desconsideradas con la religión u otras frases tendenciosas.
Más información: <https://github.com/get-alex/alex>.

- Analiza texto desde `stdin`:

`echo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">His network looks good</span>` | alex --stdin`

- Analiza todos los archivos del directorio actual:

`alex`

- Analiza un archivo dado:

`alex `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_de_texto.md</span>

- Analiza todos los archivos Markdown excepto `ejemplo.md`.:

`alex *.md !`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/hacia/ejemplo.md</span>
