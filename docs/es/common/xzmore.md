---
layout: page
title: common/xzmore (español)
description: "Muestra texto de archivos comprimidos `xz` o `lzma`."
content_hash: a7b05235c7e15d8a5d13f04322ad25b188428802
last_modified_at: 2024-11-17
related_topics:
  - title: English version
    url: /en/common/xzmore.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/xzmore.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/xzmore.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/xzmore.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># xzmore

Muestra texto de archivos comprimidos `xz` o `lzma`.
Casi equivalente a `xzless`, excepto que respeta la variable de entorno `PAGER`, utiliza `more` de forma predeterminada y no puede pasar opciones al paginador.
Más información: <https://manned.org/xzmore>.

- Muestra un archivo comprimido:

`xzmore `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
