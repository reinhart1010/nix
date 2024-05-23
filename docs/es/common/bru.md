---
layout: page
title: common/bru (español)
description: "CLI para Bruno, un IDE de código abierto para explorar y probar APIs."
content_hash: bd1fde0091f5b7590a804e54fe368b74bd1af489
last_modified_at: 2024-05-23
related_topics:
  - title: English version
    url: /en/common/bru.html
    icon: bi bi-globe
tldri18n_status: 2
---
# bru

CLI para Bruno, un IDE de código abierto para explorar y probar APIs.
Más información: <https://docs.usebruno.com/bru-cli/overview>.

- Ejecuta todos los archivos de petición en el directorio actual:

`bru run`

- Ejecuta una única petición en el directorio actual especificando su nombre de archivo:

`bru run `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">archivo.bru</span>

- Ejecuta peticiones utilizando un entorno:

`bru run --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_entorno</span>

- Ejecuta peticiones utilizando un entorno con una variable:

`bru run --env `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_entorno</span>` --env-var `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">nombre_variable</span>`=`<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">valor_variable</span>

- Ejecuta la solicitud y guarda los resultados en un archivo de salida:

`bru run --output `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/a/archivo_de_salida.json</span>

- Muestra ayuda:

`bru run --help`
