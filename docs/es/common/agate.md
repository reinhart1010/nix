---
layout: page
title: common/agate (español)
description: "Un sencillo servidor para el protocolo de red Gemini."
content_hash: ce330c420662fed9a5fcc5b95734cb35e846ed57
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/agate.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/agate.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/agate.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/agate.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/agate.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/agate.html
    icon: bi bi-globe
tldri18n_status: 2
---
# agate

Un sencillo servidor para el protocolo de red Gemini.
Más información: <https://github.com/mbrubeck/agate>.

- Ejecuta y genera una clave privada y un certificado:

`agate --content `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/contenido/</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">[::]:1965</span>` --addr `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">0.0.0.0:1965</span>` --hostname `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ejemplo.com</span>` --lang `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">sp-SP</span>

- Ejecuta servidor:

`agate `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra la ayuda:

`agate -h`
