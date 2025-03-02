---
layout: page
title: common/wc (español)
description: "Cuenta líneas, palabras, y bytes."
content_hash: 02ff8ba4fe19c6b3c1e294f5b8f746ecdfb3f8d7
last_modified_at: 2025-03-02
related_topics:
  - title: English version
    url: /en/common/wc.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/wc.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/wc.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/wc.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/common/wc.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/wc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wc

Cuenta líneas, palabras, y bytes.
Más información: <https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>.

- Cuenta todas las líneas en un archivo:

`wc --lines `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Cuenta todas las palabras en un archivo:

`wc --words `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Cuenta todos los bytes en un archivo:

`wc --bytes `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Cuenta todos los caracteres en un archivo (considerando los caracteres de varios bytes):

`wc --chars `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Cuenta todas las líneas, palabras y bytes desde `stdin`:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`

- Cuenta la longitud de la línea más larga en número de caracteres:

`wc --max-line-length `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
