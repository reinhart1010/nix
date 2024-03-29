---
layout: page
title: osx/xattr (español)
description: "Utilidad para trabajar con atributos extendidos del sistema de ficheros."
content_hash: 661431eb338e717b3515edd457633ddbf7b21686
last_modified_at: 2024-01-31
related_topics:
  - title: English version
    url: /en/osx/xattr.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/xattr.html
    icon: bi bi-globe
tldri18n_status: 2
---
# xattr

Utilidad para trabajar con atributos extendidos del sistema de ficheros.
Más información: <https://keith.github.io/xcode-man-pages/xattr.1.html>.

- Lista atributos extendidos clave:valor para un archivo dado:

`xattr -l `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Escribe un atributo para un archivo determinado:

`xattr -w `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">atributo_clave</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">atributo_valor</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Elimina un atributo de un archivo determinado:

`xattr -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">com.apple.quarantine</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Elimina todos los atributos extendidos de un archivo determinado:

`xattr -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Elimina recursivamente un atributo en un directorio determinado:

`xattr -rd `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">clave_atributo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">directorio</span>
