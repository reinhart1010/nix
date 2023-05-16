---
layout: page
title: common/asciidoctor (español)
description: "Un procesador que convierte archivos AsciiDoc a un formato publicable."
content_hash: 5d494644043397a857c862c19799efe11462b45b
last_modified_at: 2023-04-21
related_topics:
  - title: English version
    url: /en/common/asciidoctor.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asciidoctor.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/asciidoctor.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/asciidoctor.html
    icon: bi bi-globe
---

This entry is very new in the [tldr-pages](https://github.com/tldr-pages/tldr) project, hence translation data is currently unavailable for a while.

<hr># asciidoctor

Un procesador que convierte archivos AsciiDoc a un formato publicable.
Más información: <https://docs.asciidoctor.org>.

- Convierte un archivo `.adoc` específico a HTML (el formato de salida por defecto):

`asciidoctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.adoc</span>

- Convierte un archivo `.adoc` específico a HTML y vincula una hoja de estilos CSS:

`asciidoctor -a stylesheet=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/stylesheet.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.adoc</span>

- Convierte un archivo específico `.adoc` en HTML incrustable, eliminando todo excepto el cuerpo:

`asciidoctor --embedded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.adoc</span>

- Convierte un archivo `.adoc` dado en un PDF utilizando la biblioteca `asciidoctor-pdf`:

`asciidoctor --backend=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` --require=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asciidoctor-pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.adoc</span>