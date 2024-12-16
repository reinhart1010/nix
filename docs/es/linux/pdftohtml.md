---
layout: page
title: linux/pdftohtml (español)
description: "Convierte archivos PDF a HTML, XML e imágenes PNG."
content_hash: ba3e8d31ad55a361f5d192225fc2ab9fb61b6eb0
last_modified_at: 2024-12-16
related_topics:
  - title: English version
    url: /en/linux/pdftohtml.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pdftohtml.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/linux/pdftohtml.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># pdftohtml

Convierte archivos PDF a HTML, XML e imágenes PNG.
Más información: <https://manned.org/pdftohtml>.

- Convierte un archivo PDF en un archivo HTML:

`pdftohtml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_resultado.html</span>

- Ignora imágenes en el archivo PDF:

`pdftohtml -i `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_resultado.html</span>

- Genera un único archivo HTML que incluye todas las páginas PDF:

`pdftohtml -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_resultado.html</span>

- Convierte un archivo PDF en un archivo XML:

`pdftohtml -xml `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_resultado.xml</span>
