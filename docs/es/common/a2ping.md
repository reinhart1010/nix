---
layout: page
title: common/a2ping (español)
description: "Convierte imágenes en archivos EPS o PDF."
content_hash: 1e678ba87e5f70a3ab23a621bdd871bad0470130
last_modified_at: 2023-11-23
related_topics:
  - title: বাংলা version
    url: /bn/common/a2ping.html
    icon: bi bi-globe
  - title: English version
    url: /en/common/a2ping.html
    icon: bi bi-globe
  - title: हिन्दी version
    url: /hi/common/a2ping.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/a2ping.html
    icon: bi bi-globe
  - title: Nederlands version
    url: /nl/common/a2ping.html
    icon: bi bi-globe
tldri18n_status: 0
---

### Outdated Translation
This entry is currently considered outdated and its contents may not be up-to-date with other translations.

Please considering fixing this issue by contributing to the [tldr-pages](https://github.com/tldr-pages/tldr) project directly.

<a class="btn btn-primary" href="{{ site.url }}/en/common/a2ping.html">View original (English) version</a>
<a class="btn" href="https://github.com/tldr-pages/tldr/blob/main/CONTRIBUTING.md">Contributing Guidelines</a>

<hr># a2ping

Convierte imágenes en archivos EPS o PDF.
Más información: <https://manned.org/a2ping>.

- Convierte una imagen a PDF (Nota: Especificar un nombre de archivo de salida es opcional):

`a2ping `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/imagen.ext</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/salida.pdf</span>

- Comprime el documento utilizando el método especificado:

`a2ping --nocompress `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">none|zip|best|flate</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Escanea HiResBoundingBox si está presente (Nota: por defecto es sí):

`a2ping --nohires `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Permite el contenido de la página por debajo y a la izquierda del origen (Nota: por defecto es no):

`a2ping --below `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Pasa argumentos adicionales a `gs`:

`a2ping --gsextra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Pasa argumentos adicionales a un programa externo (por ejemplo, `pdftops`):

`a2ping --extra `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">argumentos</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Muestra ayuda:

`a2ping -h`
