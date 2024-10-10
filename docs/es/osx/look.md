---
layout: page
title: osx/look (español)
description: "Muestra las líneas que empiezan por un prefijo en un archivo ordenado."
content_hash: 752078548c672ec3dd858cb5cae77b5a4a9702ea
last_modified_at: 2024-10-10
related_topics:
  - title: English version
    url: /en/osx/look.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/osx/look.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/osx/look.html
    icon: bi bi-globe
tldri18n_status: 1
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># look

Muestra las líneas que empiezan por un prefijo en un archivo ordenado.
Vea también: `grep`, `sort`.
Más información: <https://keith.github.io/xcode-man-pages/look.1.html>.

- Busca líneas que comiencen con un prefijo específico en un archivo específico:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefijo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Búsqueda insensible a mayúsculas y minúsculas solo en caracteres alfanuméricos:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--ignore-case</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--alphanum</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefijo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Especifica un carácter de terminación de cadena (espacio por defecto):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--terminate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- Busca en `/usr/share/dict/words` (se asumen `--ignore-case` y `--alphanum`):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefijo</span>
