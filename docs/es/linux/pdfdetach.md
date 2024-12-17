---
layout: page
title: linux/pdfdetach (español)
description: "Lista o extrae archivos adjuntos (archivos embebidos) de un archivo PDF."
content_hash: 605c0fbbd1fcf4c80fc82bf977833d681d94490f
last_modified_at: 2024-12-17
related_topics:
  - title: English version
    url: /en/linux/pdfdetach.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/linux/pdfdetach.html
    icon: bi bi-globe
tldri18n_status: 2
---
# pdfdetach

Lista o extrae archivos adjuntos (archivos embebidos) de un archivo PDF.
Vea también: `pdfattach`, `pdfimages`, `pdfinfo`.
Más información: <https://manned.org/pdfdetach>.

- Lista todos los archivos adjuntos en un archivo con una codificación de texto específica:

`pdfdetach list -enc `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">UTF-8</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pdf</span>

- Guarda un archivo embebido especificado por su número:

`pdfdetach -save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.pdf</span>

- Guarda un archivo embebido especificando su nombre:

`pdfdetach -savefile `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo.pdf</span>

- Guarda el archivo embebido con un nombre de archivo de salida personalizado:

`pdfdetach -save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/resultado</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.pdf</span>

- Guarda el adjunto desde un archivo protegido por contraseña del propietario/usuario:

`pdfdetach -save `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">número</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">-opw|-upw</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">contraseña</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/la/entrada.pdf</span>
