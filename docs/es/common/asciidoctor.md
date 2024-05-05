---
layout: page
title: common/asciidoctor (español)
description: "Un procesador que convierte archivos AsciiDoc a un formato publicable."
content_hash: f0b2ba4ca96dc9e8676a4fd839fc265d9b6d2832
last_modified_at: 2024-05-05
related_topics:
  - title: English version
    url: /en/common/asciidoctor.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/asciidoctor.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/asciidoctor.html
    icon: bi bi-globe
  - title: português (Brasil) version
    url: /pt_BR/common/asciidoctor.html
    icon: bi bi-globe
  - title: русский version
    url: /ru/common/asciidoctor.html
    icon: bi bi-globe
tldri18n_status: 2
---
# asciidoctor

Un procesador que convierte archivos AsciiDoc a un formato publicable.
Más información: <https://docs.asciidoctor.org>.

- Convierte un archivo `.adoc` específico a HTML (el formato de salida por defecto):

`asciidoctor `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.adoc</span>

- Convierte un archivo `.adoc` específico a HTML y vincula una hoja de estilos CSS:

`asciidoctor -a stylesheet `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/stylesheet.css</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.adoc</span>

- Convierte un archivo específico `.adoc` en HTML incrustable, eliminando todo excepto el cuerpo:

`asciidoctor --embedded `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.adoc</span>

- Convierte un archivo `.adoc` dado en un PDF utilizando la biblioteca `asciidoctor-pdf`:

`asciidoctor --backend `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">pdf</span>` --require `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">asciidoctor-pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.adoc</span>
