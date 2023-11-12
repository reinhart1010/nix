---
layout: page
title: common/atoum (español)
description: "Un framework de pruebas unitarias para PHP sencillo, moderno e intuitivo."
content_hash: d22f9baefb6de4e39d4e947d62328fe223aef9ab
last_modified_at: 2023-11-12
related_topics:
  - title: English version
    url: /en/common/atoum.html
    icon: bi bi-globe
  - title: français version
    url: /fr/common/atoum.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/atoum.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/atoum.html
    icon: bi bi-globe
tldri18n_status: 2
---
# atoum

Un framework de pruebas unitarias para PHP sencillo, moderno e intuitivo.
Más información: <http://atoum.org>.

- Inicializa un fichero de configuración:

`atoum --init`

- Ejecuta todas las pruebas:

`atoum`

- Ejecuta pruebas utilizando el archivo de configuración especificado:

`atoum -c `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Ejecuta un archivo de prueba específico:

`atoum -f `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>

- Ejecuta un directorio específico de pruebas:

`atoum -d `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/directorio</span>

- Ejecuta todas las pruebas dado un namespace específico:

`atoum -ns `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">namespace</span>

- Ejecuta todas las pruebas dada una etiqueta específica:

`atoum -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">etiqueta</span>

- Carga un archivo bootstrap personalizado antes de ejecutar las pruebas:

`atoum --bootstrap-file `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/archivo</span>
