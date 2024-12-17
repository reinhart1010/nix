---
layout: page
title: linux/pdfattach (español)
description: "Agrega un nuevo archivo adjunto (incorporándolo) a un archivo PDF existente."
content_hash: 6d90af813c14a8e4cddb86ff8b0d8f9e0afe7091
last_modified_at: 2024-12-17
related_topics:
  - title: English version
    url: /en/linux/pdfattach.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pdfattach.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdfattach

Agrega un nuevo archivo adjunto (incorporándolo) a un archivo PDF existente.
Vea también: `pdfdetach`, `pdfimages`, `pdfinfo`.
Más información: <https://manned.org/pdfattach>.

- Añade un nuevo adjunto a un archivo PDF existente:

`pdfattach `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_original.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_a_adjuntar</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pdf</span>

- Reemplaza el adjunto del mismo nombre, si existe:

`pdfattach -replace `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_original.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo_adjunto</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado.pdf</span>

- Muestra la ayuda:

`pdfattach -h`

- Muestra la versión:

`pdfattach -v`
