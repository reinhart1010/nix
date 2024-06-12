---
layout: page
title: freebsd/look (español)
description: "Muestra las líneas que empiezan con un prefijo en un archivo ordenado."
content_hash: 24e077a3ea3ccbf2de3ca73b9dcf6e600debf6b4
last_modified_at: 2024-06-12
related_topics:
  - title: English version
    url: /en/freebsd/look.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/freebsd/look.html
    icon: bi bi-globe
tldri18n_status: 2
---
# look

Muestra las líneas que empiezan con un prefijo en un archivo ordenado.
Vea también: `grep`, `sort`.
Más información: <https://man.freebsd.org/cgi/man.cgi?look>.

- Busca líneas que comiencen con un prefijo específico en un archivo específico:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefijo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Busca caracteres alfanuméricos sin tomar en cuenta las mayúsculas o minúsculas:

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-f|--ignore-case</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-d|--alphanum</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefijo</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Especifica un carácter de terminación de cadena (un espacio por defecto):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-t|--terminate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">,</span>

- Busca en `/usr/share/dict/words` (se asumen `--ignore-case` y `--alphanum`):

`look `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">prefijo</span>
