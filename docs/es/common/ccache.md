---
layout: page
title: common/ccache (español)
description: "Caché del compilador C/C++."
content_hash: 3408805c7cb912c5c965370e5b4fea2f64f3bb41
last_modified_at: 2024-02-03
related_topics:
  - title: English version
    url: /en/common/ccache.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/ccache.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># ccache

Caché del compilador C/C++.
Nota: los paquetes suelen proporcionar enlaces simbólicos para los compiladores en `/usr/lib/ccache/bin`. Anteponga este directorio en `$PATH` para utilizar automáticamente `ccache` con los compiladores.
Más información: <https://ccache.dev/manual/latest.html>.

- Muestra las e[s]tadísticas de la caché actual:

`ccache --show-stats`

- Borra toda la caché:

`ccache --clear`

- Restablece ([z]ero) las estadísticas (pero no la propia caché):

`ccache --zero-stats`

- Compila código C y almacena la salida compilada en la caché (para usar `ccache` en todas las invocaciones de `gcc`, lea la nota anterior):

`ccache gcc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.c</span>
