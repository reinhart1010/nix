---
layout: page
title: osx/wc (español)
description: "Cuenta líneas, palabras o bytes."
content_hash: 57778e1c2537a47d62b4478388d5d3a42396abd2
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/osx/wc.html
    icon: bi bi-globe
  - title: polski version
    url: /pl/osx/wc.html
    icon: bi bi-globe
tldri18n_status: 2
---
# wc

Cuenta líneas, palabras o bytes.
Más información: <https://ss64.com/osx/wc.html>.

- Cuenta líneas en un archivo:

`wc -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Cuenta palabras en el archivo:

`wc -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Cuenta caracteres (bytes) en el archivo:

`wc -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Cuenta caracteres en el archivo (teniendo en cuenta los conjuntos de caracteres multibyte):

`wc -m `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Usa `stdin` para contar líneas, palabras y caracteres (bytes) en ese orden:

<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">find .</span>` | wc`
