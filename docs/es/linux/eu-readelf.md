---
layout: page
title: linux/eu-readelf (español)
description: "Muestra información sobre archivos ELF."
content_hash: 4fdfb4630c711c202bf94d7d16b5528656a0aae9
last_modified_at: 2024-04-17
related_topics:
  - title: English version
    url: /en/linux/eu-readelf.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/eu-readelf.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># eu-readelf

Muestra información sobre archivos ELF.
Más información: <https://manned.org/eu-readelf>.

- Muestra toda la información extraíble en un archivo ELF:

`eu-readelf --all `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra el contenido de todos los segmentos y secciones de NOTE, o de un segmento o sección en particular:

`eu-readelf --notes[=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">.note.ABI-tag</span>`] `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/fichero</span>
