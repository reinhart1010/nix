---
layout: page
title: common/cpdf (español)
description: "Interfaz de línea de comandos para manipular documentos PDF existentes de diferentes maneras."
content_hash: a8f0c14229e2c2a47e9e4ff8203ee70f443721ad
related_topics:
  - title: English version
    url: /en/common/cpdf.html
    icon: bi bi-globe
---
# cpdf

Interfaz de línea de comandos para manipular documentos PDF existentes de diferentes maneras.
Más información: <https://www.coherentpdf.com/cpdfmanual/cpdfmanual.html>.

- Selecciona las páginas 1, 2, 3 y 6 del documento fuente y escribirlas en el documento objetivo:

`cpdf `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/documento_fuente.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">1-3,6</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/documento_objetivo.pdf</span>

- Fusiona dos documentos en uno nuevo:

`cpdf -merge `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/documento_fuente_uno.pdf</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/documento_fuente_dos.pdf</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/documento_objetivo.pdf</span>

- Muestra los marcadores del documento:

`cpdf -list-bookmarks `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/documento.pdf</span>

- Divide un documento en trozos de diez páginas, escribiendo `fragmento001.pdf`, `fragmento002.pdf`, etc:

`cpdf -split `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/documento.pdf</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/fragmento%%%.pdf</span>` -chunk 10`

- Encripta un documento utilizando encriptado 128bit y establece `fred` como la contraseña del propietario y `joe` como la contraseña de usuario:

`cpdf -encrypt 128bit fred joe `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/documento_fuente.pdf</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/documento_encriptado.pdf</span>

- Desencripta un documento utilizando la contraseña del propietario (`fred`):

`cpdf -decrypt `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/documento_encriptado.pdf</span>` owner=fred -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/documento_desencriptado.pdf</span>

- Muestra las anotaciones de un documento:

`cpdf -list-annotations `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/documento.pdf</span>

- Crea un nuevo documento, con metadatos, a partir de uno que ya existe:

`cpdf -set-metadata `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/de/los/metadatos.xml</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/documento_fuente.pdf</span>` -o `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">ruta/al/documento_objetivo.pdf</span>
