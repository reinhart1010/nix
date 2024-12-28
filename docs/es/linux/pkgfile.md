---
layout: page
title: linux/pkgfile (español)
description: "Busca archivos en los paquetes de los repositorios oficiales en sistemas basados en Arch."
content_hash: 8acc4dfa0552f9f15aa13149ce2fa569fae2705b
last_modified_at: 2024-12-28
related_topics:
  - title: English version
    url: /en/linux/pkgfile.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pkgfile.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pkgfile.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pkgfile

Busca archivos en los paquetes de los repositorios oficiales en sistemas basados en Arch.
Vea también: `pacman files`, que describe el uso de `pacman --files`.
Más información: <https://manned.org/pkgfile>.

- Sincroniza la base de datos pkgfile:

`sudo pkgfile --update`

- Busca un paquete que posee un archivo específico:

`pkgfile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Lista todos los archivos proporcionados por un paquete:

`pkgfile --list `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Lista los ejecutables proporcionados por un paquete:

`pkgfile --list --binaries `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">paquete</span>

- Busca un paquete que posee un archivo específico utilizando coincidencias insensibles a mayúsculas y minúsculas:

`pkgfile --ignorecase `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Busca un paquete que posee un archivo específico en el directorio `bin` o `sbin`:

`pkgfile --binaries `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Busca un paquete que posee un archivo específico, mostrando la versión del paquete:

`pkgfile --verbose `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>

- Busca un paquete que posee un archivo específico en un repositorio específico:

`pkgfile --repo `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_del_repositorio</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo</span>
